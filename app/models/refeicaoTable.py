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
            "confirmacoes": self.confirmacoes(),
            "avaliacao_media": self.avaliacao_media(),
        }

        return output

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Refeicao %r>" % self.id

    # --------------------------------------------------------------------------------------------------#

    def avaliacao_media(self):
        avaliacao_media = 0
        avaliacao_count = 0

        for avaliacao in self.avaliacoes:
            avaliacao_media = avaliacao_media + avaliacao.nota
            avaliacao_count = avaliacao_count + 1

        if avaliacao_count > 0:
            avaliacao_media = avaliacao_media / avaliacao_count
        
        return avaliacao_media

    # --------------------------------------------------------------------------------------------------#

    def confirmacoes(self):
        confirm_y = 0
        confirm_n = 0

        for confirmacao in self.alunos:
            if confirmacao.confirmado:
                confirm_y = confirm_y + 1
            else:
                confirm_n = confirm_n + 1
        
        return {
            "sim": confirm_y,
            "nao": confirm_n
        }