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
            "descricao": self.descricao,
            "avaliacao_media": self.avaliacao_media(),
        }

        return output

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Prato %r>" % self.id

    # --------------------------------------------------------------------------------------------------#

    def avaliacao_media(self):
        avaliacao_media = 0
        avaliacao_count = 0

        for refeicao in self.refeicoes:
            avaliacao_media = avaliacao_media + refeicao.avaliacao_media()
            avaliacao_count = avaliacao_count + 1
        
        if avaliacao_count > 0:
            avaliacao_media = avaliacao_media / avaliacao_count
        
        return avaliacao_media