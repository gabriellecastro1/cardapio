from app import app, db, Messages
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc, or_
from . import resource, paginate, field_validator
from app import Prato
from app import fieldsFormatter

from flask_pydantic import validate
from app import PratoAddSchema


@app.route("/prato/all", methods=["GET"])
@jwt_required
@resource("prato-all")
def pratoAll():
    page = request.args.get("page", 1, type=int)
    rows_per_page = request.args.get("rows_per_page", app.config["ROWS_PER_PAGE"], type=int)
    descricao = request.args.get("descricao", None)

    query = Prato.query

    if descricao != None:
        query = query.filter(Prato.descricao.ilike("%%{}%%".format(fieldsFormatter.CpfFormatter().clean(descricao))))

    perfis, output = paginate(query, page, rows_per_page)

    for perfil in perfis:
        data = perfil.to_dict()
        output["itens"].append(data)

    return jsonify(output)


# --------------------------------------------------------------------------------------------------#


@app.route("/prato/view/<int:prato_id>", methods=["GET"])
@jwt_required
@resource("prato-view")
def pratoView(prato_id: int):

    prato = Prato.query.get(prato_id)

    if not prato:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(prato_id), "error": True}
        )

    data = prato.to_dict()
    data['error'] = False

    return jsonify(data)


# --------------------------------------------------------------------------------------------------#

@app.route("/prato/add", methods=["POST"])
@jwt_required
@resource("prato-add")
@field_validator(PratoAddSchema)
def pratoAdd():

    data = request.get_json()

    prato = Prato(
        descricao=data.get("descricao"),
    )

    db.session.add(prato)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Prato"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/prato/edit/<int:prato_id>", methods=["PUT"])
@jwt_required
@resource("prato-edit")
@field_validator(PratoAddSchema)
def pratoEdit(prato_id: int):
    data = request.get_json()
    prato = Prato.query.get(prato_id)

    if not prato:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(prato_id), "error": True}
        )

    prato.descricao = data.get("descricao")
    
    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_UPDATED.format("Prato"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/prato/delete/<int:prato_id>", methods=["DELETE"])
@jwt_required
@resource("prato-delete")
def pratoDelete(prato_id: int):
    prato = Prato.query.get(prato_id)

    if not prato:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(prato_id), "error": True}
        )

    db.session.delete(prato)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format("Prato"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        return jsonify(
            {"message": Messages.REGISTER_DELETE_INTEGRITY_ERROR, "error": True}
        )
