from app import db

class Avaliacao(db.Model):
    __tablename__ = "avaliacao"

    id = db.Column(db.BigInteger, primary_key=True)
    refeicao_id = db.Column(db.BigInteger, db.ForeignKey("refeicao.id"), nullable=False)
    nota = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.Text, nullable=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, refeicao_id, nota, comentario):
        self.refeicao_id = refeicao_id
        self.nota = nota
        self.comentario = comentario

    # --------------------------------------------------------------------------------------------------#

    def to_dict(self):
        output = {
            "id": self.id,
            "refeicao_id": self.refeicao_id,
            "nota": self.nota,
            "comentario": self.comentario
        }

        return output

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Avaliacao %r>" % self.id