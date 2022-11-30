from app import db

class TipoRefeicao(db.Model):
    __tablename__ = "tipo_refeicao"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)

    refeicoes = db.relationship("Refeicao", backref="tipo_refeicao", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, nome):
        self.nome = nome

    # --------------------------------------------------------------------------------------------------#

    def to_dict(self):
        output = {
            "id": self.id,
            "nome": self.nome
        }

        return output

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Refeicao %r>" % self.id