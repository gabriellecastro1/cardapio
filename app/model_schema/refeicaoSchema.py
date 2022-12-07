from typing import Optional
from pydantic import BaseModel, constr, conint
import json

class RefeicaoAddSchema(BaseModel):
    # mandatory field
    descricao: constr(min_length=2)
    tipo_refeicao_id: int
    cardapio_id: int
    prato_id: int
    
    class Config:
        json_loads = json.loads

class RefeicaoAvaliarSchema(BaseModel):
    # mandatory field
    nota: conint(gt= 0, lt= 6)
    comentario: Optional[constr(min_length=0)]
    refeicao_id: int
    
    class Config:
        json_loads = json.loads

