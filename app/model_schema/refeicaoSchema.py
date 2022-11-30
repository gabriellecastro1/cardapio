from typing import Optional
from pydantic import BaseModel, constr
import json

class RefeicaoAddSchema(BaseModel):
    # mandatory field
    descricao: constr(min_length=2)
    tipo_refeicao_id: int
    cardapio_id: int
    prato_id: int
    
    class Config:
        json_loads = json.loads
