from app import db

class Cardapio(db.Model):
    __tablename__ = "cardapio"

    id = db.Column(db.BigInteger, primary_key=True)
    data = db.Column(db.Date, nullable=False)

    refeicoes = db.relationship("Refeicao", backref="cardapio", lazy=True)
    
    # --------------------------------------------------------------------------------------------------#

    def __init__(self, data):
        self.data = data
        
    # --------------------------------------------------------------------------------------------------#

    def to_dict(self):
        output = {
            "id": self.id,
            "data": self.data
        }

        return output

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<Cardapio %r>" % self.cardapio