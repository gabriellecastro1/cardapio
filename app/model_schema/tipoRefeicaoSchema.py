from typing import Optional
from pydantic import BaseModel, constr
import json

class TipoRefeicaoAddSchema(BaseModel):
    # mandatory field
    nome: constr(min_length=2, max_length=255)
    
    class Config:
        json_loads = json.loads
