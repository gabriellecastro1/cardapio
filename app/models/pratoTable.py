from app import db

class Prato(db.Model):
    __tablename__ = "prato"

    id = db.Column(db.BigInteger, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)

    refeicoes = db.relationship("Refeicao", backref="prato", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, descricao):
        self.descricao = descricao

    # --------------------------------------------------------------------------------------------------#

    def to_dict(self):
        output = {
            "id": self.id,
            "descricao": self.descricao
        }

        return output

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Prato %r>" % self.id