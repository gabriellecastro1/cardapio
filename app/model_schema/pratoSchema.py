from typing import Optional
from pydantic import BaseModel, constr
import json

class PratoAddSchema(BaseModel):
    # mandatory field
    descricao: constr(min_length=2, max_length=255)
    
    class Config:
        json_loads = json.loads