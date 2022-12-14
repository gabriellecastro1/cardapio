from typing import Optional
import re
from pydantic import BaseModel, constr, validator
import json

class AlunoAddSchema(BaseModel):
    # mandatory field
    matricula: constr(min_length=2, max_length=20)
    nome: constr(min_length=2, max_length=20)
    email: constr(min_length=2, max_length=255)

    class Config:
        json_loads = json.loads

    @validator('email')
    def email_validator(cls, email):
        email = email.lower()
        if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) is None:
            raise ValueError('O email informado é invalido.')
        return email


class AlunoConfirmarSchema(BaseModel):
    # mandatory field
    matricula: constr(min_length=2, max_length=20)
    confirmado: bool
    refeicao_id: int

    class Config:
        json_loads = json.loads