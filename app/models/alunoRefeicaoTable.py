from app import db

class AlunoRefeicao(db.Model):
    __tablename__ = "aluno_refeicao"

    matricula = db.Column(db.String(20), db.ForeignKey("aluno.matricula"), nullable=False, primary_key=True)
    refeicao_id = db.Column(db.BigInteger, db.ForeignKey("refeicao.id"), nullable=False, primary_key=True)
    confirmado = db.Column(db.Boolean, nullable=False)
    

    # --------------------------------------------------------------------------------------------------#

    def __init__(self, matricula, refeicao_id, confirmado=False):
        self.matricula = matricula
        self.refeicao_id = refeicao_id
        self.confirmado = confirmado
        
    # --------------------------------------------------------------------------------------------------#

    def to_dict(self):
        output = {
            "matricula": self.matricula,
            "refeicao_id": self.refeicao_id,
            "confirmado": self.confirmado,
        }

        return output

    # --------------------------------------------------------------------------------------------------#

    def __repr__(self):
        return "<AlunoRefeicao {} {} {}>".format(self.matricula, self.refeicao_id, self.confirmado)