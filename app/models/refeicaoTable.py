from app import db

class Refeicao(db.Model):
    __tablename__ = "refeicao"

    id = db.Column(db.BigInteger, primary_key=True)
    descricao = db.Column(db.Text, nullable=False)
    tipo_refeicao_id = db.Column(db.Integer, db.ForeignKey("tipo_refeicao.id"), nullable=False)
    cardapio_id = db.Column(db.BigInteger, db.ForeignKey("cardapio.id"), nullable=False)
    prato_id = db.Column(db.BigInteger, db.ForeignKey("prato.id"), nullable=False)

    alunos = db.relationship("AlunoRefeicao", backref="refeicao", lazy=True)
    avaliacoes = db.relationship("Avaliacao", backref="refeicao", lazy=True)

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, descricao, tipo_refeicao_id, cardapio_id, prato_id):
        self.descricao = descricao
        self.tipo_refeicao_id = tipo_refeicao_id
        self.cardapio_id = cardapio_id
        self.prato_id = prato_id

    # --------------------------------------------------------------------------------------------------#

    def to_dict(self):
        output = {
            "id": self.id,
            "descricao": self.descricao,
            "tipo_refeicao_id": self.tipo_refeicao_id,
            "cardapio_id": self.cardapio_id,
            "cardapio": self.cardapio.to_dict(),
            "prato_id": self.prato_id,
            "prato": self.prato.to_dict(),
        }

        return output

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Refeicao %r>" % self.id