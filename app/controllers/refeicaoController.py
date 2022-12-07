from app import app, db, Messages
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy import exc, or_
from . import resource, paginate, field_validator
from app import Refeicao, Avaliacao
from app import fieldsFormatter

from app import RefeicaoAddSchema, RefeicaoAvaliarSchema


@app.route("/refeicao/all", methods=["GET"])
# @jwt_required
# @resource("refeicao-all")
def refeicaoAll():
    page = request.args.get("page", 1, type=int)
    rows_per_page = request.args.get("rows_per_page", app.config["ROWS_PER_PAGE"], type=int)
    descricao = request.args.get("descricao", None)
    prato_id = request.args.get("prato_id", None)

    query = Refeicao.query

    if descricao != None:
        query = query.filter(Refeicao.descricao.ilike("%%{}%%".format(descricao)))
    
    if prato_id != None:
        query = query.filter(Refeicao.prato_id == prato_id)

    refeicoes, output = paginate(query, page, rows_per_page)

    for refeicao in refeicoes:
        data = refeicao.to_dict()
        output["itens"].append(data)

    return jsonify(output)


# --------------------------------------------------------------------------------------------------#


@app.route("/refeicao/view/<int:refeicao_id>", methods=["GET"])
# @jwt_required
# @resource("refeicao-view")
def refeicaoView(refeicao_id: int):

    refeicao = Refeicao.query.get(refeicao_id)

    if not refeicao:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(refeicao_id), "error": True}
        )

    data = refeicao.to_dict()
    data['error'] = False

    return jsonify(data)


# --------------------------------------------------------------------------------------------------#

@app.route("/refeicao/add", methods=["POST"])
@jwt_required
@resource("refeicao-add")
@field_validator(RefeicaoAddSchema)
def refeicaoAdd():

    data = request.get_json()

    refeicao = Refeicao(
        descricao=data.get("descricao"),
        tipo_refeicao_id=data.get("tipo_refeicao_id"),
        prato_id=data.get("prato_id"),
        cardapio_id=data.get("cardapio_id")
    )

    db.session.add(refeicao)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Refeição"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/refeicao/edit/<int:refeicao_id>", methods=["PUT"])
@jwt_required
@resource("refeicao-edit")
@field_validator(RefeicaoAddSchema)
def refeicaoEdit(refeicao_id: int):
    data = request.get_json()
    refeicao = Refeicao.query.get(refeicao_id)

    if not refeicao:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(refeicao_id), "error": True}
        )

    refeicao.descricao = data.get("descricao")
    refeicao.tipo_refeicao_id=data.get("tipo_refeicao_id")
    refeicao.prato_id=data.get("prato_id")
    refeicao.cardapio_id=data.get("cardapio_id")
    
    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_UPDATED.format("Refeição"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/refeicao/delete/<int:refeicao_id>", methods=["DELETE"])
@jwt_required
@resource("refeicao-delete")
def refeicaoDelete(refeicao_id: int):
    refeicao = Refeicao.query.get(refeicao_id)

    if not refeicao:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(refeicao_id), "error": True}
        )

    db.session.delete(refeicao)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format("Refeição"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        return jsonify(
            {"message": Messages.REGISTER_DELETE_INTEGRITY_ERROR, "error": True}
        )

# --------------------------------------------------------------------------------------------------#

@app.route("/refeicao/avaliar", methods=["POST"])
@field_validator(RefeicaoAvaliarSchema)
def refeicaoAvaliar():

    data = request.get_json()

    avaliacao = Avaliacao(
        nota = data.get("nota"),
        comentario = data.get("comentario"),
        refeicao_id = data.get("refeicao_id")
    )

    db.session.add(avaliacao)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Avaliação"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, "error": True}
        )
