from typing import Optional
from pydantic import BaseModel, constr
import json

class CardapioAddSchema(BaseModel):
    # mandatory field
    
    class Config:
        json_loads = json.loads