from app import app, db, Messages
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc, or_
from . import resource, paginate, field_validator
from app import Cardapio
from app import fieldsFormatter

from flask_pydantic import validate
from app import CardapioAddSchema


@app.route("/cardapio/all", methods=["GET"])
@jwt_required
@resource("cardapio-all")
def cardapioAll():
    page = request.args.get("page", 1, type=int)
    rows_per_page = request.args.get("rows_per_page", app.config["ROWS_PER_PAGE"], type=int)
    data = request.args.get("data", None)

    query = Cardapio.query

    if data != None:
        query = query.filter(Cardapio.data == data)

    cardapios, output = paginate(query, page, rows_per_page)

    for perfil in cardapios:
        data = perfil.to_dict()
        output["itens"].append(data)

    return jsonify(output)


# --------------------------------------------------------------------------------------------------#


@app.route("/cardapio/view/<int:cardapio_id>", methods=["GET"])
@jwt_required
@resource("cardapio-view")
def cardapioView(cardapio_id: int):

    cardapio = Cardapio.query.get(cardapio_id)

    if not cardapio:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(cardapio_id), "error": True}
        )

    data = cardapio.to_dict()
    data['error'] = False

    return jsonify(data)


# --------------------------------------------------------------------------------------------------#

@app.route("/cardapio/add", methods=["POST"])
@jwt_required
@resource("cardapio-add")
@field_validator(CardapioAddSchema)
def cardapioAdd():

    data = request.get_json()

    cardapio = Cardapio(
        data=data.get("data"),
    )

    db.session.add(cardapio)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Cardapio"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/cardapio/edit/<int:cardapio_id>", methods=["PUT"])
@jwt_required
@resource("cardapio-edit")
@field_validator(CardapioAddSchema)
def cardapioEdit(cardapio_id: int):
    data = request.get_json()
    cardapio = Cardapio.query.get(cardapio_id)

    if not cardapio:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(cardapio_id), "error": True}
        )

    cardapio.data = data.get("data")
    
    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_UPDATED.format("Cardapio"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/cardapio/delete/<int:cardapio_id>", methods=["DELETE"])
@jwt_required
@resource("cardapio-delete")
def cardapioDelete(cardapio_id: int):
    cardapio = Cardapio.query.get(cardapio_id)

    if not cardapio:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(cardapio_id), "error": True}
        )

    db.session.delete(cardapio)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format("Cardapio"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        return jsonify(
            {"message": Messages.REGISTER_DELETE_INTEGRITY_ERROR, "error": True}
        )
