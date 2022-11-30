from app import db

class Aluno(db.Model):
    __tablename__ = "aluno"

    matricula = db.Column(db.String(20), primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    refeicoes = db.relationship("AlunoRefeicao", backref="aluno", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, matricula, nome, email):
        self.matricula = matricula
        self.nome = nome
        self.email = email

    # --------------------------------------------------------------------------------------------------#

    def to_dict(self):
        output = {
            "matricula": self.matricula,
            "nome": self.nome,
            "email": self.email
        }

        return output

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Aluno %r>" % self.matricula