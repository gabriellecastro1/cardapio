from app import app, db, Messages
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy import exc, or_
from . import resource, paginate, field_validator
from app import TipoRefeicao
from app import fieldsFormatter

from flask_pydantic import validate
from app import TipoRefeicaoAddSchema


@app.route("/tipo-refeicao/all", methods=["GET"])
@jwt_required
@resource("tipoRefeicao-all")
def tipoRefeicaoAll():
    page = request.args.get("page", 1, type=int)
    rows_per_page = request.args.get("rows_per_page", app.config["ROWS_PER_PAGE"], type=int)
    nome = request.args.get("nome", None)

    query = TipoRefeicao.query

    if nome != None:
        query = query.filter(TipoRefeicao.nome.ilike("%%{}%%".format(fieldsFormatter.CpfFormatter().clean(nome))))

    tipos, output = paginate(query, page, rows_per_page)

    for tipo in tipos:
        data = tipo.to_dict()
        output["itens"].append(data)

    return jsonify(output)


# --------------------------------------------------------------------------------------------------#


@app.route("/tipo-refeicao/view/<int:tipo_refeicao_id>", methods=["GET"])
@jwt_required
@resource("tipoRefeicao-view")
def tipoRefeicaoView(tipo_refeicao_id: int):

    tipo_refeicao = TipoRefeicao.query.get(tipo_refeicao_id)

    if not tipo_refeicao:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(tipo_refeicao_id), "error": True}
        )

    data = tipo_refeicao.to_dict()
    data['error'] = False

    return jsonify(data)


# --------------------------------------------------------------------------------------------------#

@app.route("/tipo-refeicao/add", methods=["POST"])
@jwt_required
@resource("tipoRefeicao-add")
@field_validator(TipoRefeicaoAddSchema)
def tipoRefeicaoAdd():

    data = request.get_json()

    tipo_refeicao = TipoRefeicao(
        nome=data.get("nome"),
    )

    db.session.add(tipo_refeicao)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Tipo de Refeição"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/tipo-refeicao/edit/<int:tipo_refeicao_id>", methods=["PUT"])
@jwt_required
@resource("tipoRefeicao-edit")
@field_validator(TipoRefeicaoAddSchema)
def tipoRefeicaoEdit(tipo_refeicao_id: int):
    data = request.get_json()
    tipo_refeicao = TipoRefeicao.query.get(tipo_refeicao_id)

    if not tipo_refeicao:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(tipo_refeicao_id), "error": True}
        )

    tipo_refeicao.nome = data.get("nome")
    
    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_UPDATED.format("Tipo de Refeição"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/tipo-refeicao/delete/<int:tipo_refeicao_id>", methods=["DELETE"])
@jwt_required
@resource("tipoRefeicao-delete")
def tipoRefeicaoDelete(tipo_refeicao_id: int):
    tipo_refeicao = TipoRefeicao.query.get(tipo_refeicao_id)

    if not tipo_refeicao:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(tipo_refeicao_id), "error": True}
        )

    db.session.delete(tipo_refeicao)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format("Tipo de Refeição"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        return jsonify(
            {"message": Messages.REGISTER_DELETE_INTEGRITY_ERROR, "error": True}
        )
