from pydantic import BaseModel
from typing import Union

class GeneroRequests(BaseModel):
    nome: str
    descricao: str