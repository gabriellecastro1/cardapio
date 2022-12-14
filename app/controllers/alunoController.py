from app import app, db, Messages
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import exc, or_
from . import resource, paginate, field_validator
from app import Aluno, AlunoRefeicao
from app import fieldsFormatter

from flask_pydantic import validate
from app import AlunoAddSchema, AlunoConfirmarSchema

@app.route("/aluno/all", methods=["GET"])
@jwt_required
@resource("aluno-all")
def alunoAll():
    page = request.args.get("page", 1, type=int)
    rows_per_page = request.args.get("rows_per_page", app.config["ROWS_PER_PAGE"], type=int)
    nome = request.args.get("nome", None)
    matricula = request.args.get("matricula", None)

    query = Aluno.query

    if nome != None:
        query = query.filter(Aluno.nome.ilike("%%{}%%".format(nome)))

    if matricula != None:
        query = query.filter(Aluno.matricula.ilike("%%{}%%".format(matricula)))

    alunos, output = paginate(query, page, rows_per_page)

    for aluno in alunos:
        data = aluno.to_dict()
        output["itens"].append(data)

    return jsonify(output)


# --------------------------------------------------------------------------------------------------#


@app.route("/aluno/view/<matricula>", methods=["GET"])
@jwt_required
@resource("aluno-view")
def alunoView(matricula):

    aluno = Aluno.query.get(matricula)

    if not aluno:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(matricula), "error": True}
        )

    data = aluno.to_dict()
    data['error'] = False

    return jsonify(data)


# --------------------------------------------------------------------------------------------------#

@app.route("/aluno/add", methods=["POST"])
@jwt_required
@resource("aluno-add")
@field_validator(AlunoAddSchema)
def alunoAdd():

    data = request.get_json()

    aluno = Aluno(
        matricula=data.get("matricula"),
        nome=data.get("nome"),
        email=data.get("email"),
    )

    db.session.add(aluno)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Aluno"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/aluno/edit/<matricula>", methods=["PUT"])
@jwt_required
@resource("aluno-edit")
@field_validator(AlunoAddSchema)
def alunoEdit(matricula):
    data = request.get_json()
    aluno = Aluno.query.get(matricula)

    if not aluno:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(matricula), "error": True}
        )

    aluno.matricula = data.get("matricula")
    aluno.nome = data.get("nome")
    aluno.email = data.get("email")
    
    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_UPDATED.format("Aluno"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CHANGE_INTEGRITY_ERROR, "error": True}
        )


# --------------------------------------------------------------------------------------------------#


@app.route("/aluno/delete/<matricula>", methods=["DELETE"])
@jwt_required
@resource("aluno-delete")
def alunoDelete(matricula):
    aluno = Aluno.query.get(matricula)

    if not aluno:
        return jsonify(
            {"message": Messages.REGISTER_NOT_FOUND.format(matricula), "error": True}
        )
    
    db.session.delete(aluno)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_DELETED.format("Aluno"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        return jsonify(
            {"message": Messages.REGISTER_DELETE_INTEGRITY_ERROR, "error": True}
        )

# --------------------------------------------------------------------------------------------------#

@app.route("/aluno/confirmar", methods=["POST"])
@field_validator(AlunoConfirmarSchema)
def alunoConfirmar():

    data = request.get_json()

    alunoRefeicao = AlunoRefeicao(
        matricula=data.get("matricula"),
        refeicao_id=data.get("refeicao_id"),
        confirmado=data.get("confirmado"),
    )

    db.session.add(alunoRefeicao)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Confirmação"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, "error": True}
        )
