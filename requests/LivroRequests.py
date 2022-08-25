from datetime import date
from pydantic import BaseModel
from typing import Union

class LivroRequests(BaseModel):
    isbn: str
    titulo: str
    descricao: str
    volume: int
    palavraChave1: str
    palavraChave2: str
    palavraChave3: str
    ano: int
    edicao: int
    idEditora: int
    idGenero: int

class FilterRequests(BaseModel):
    titulo: Union[str, None] = None
    descricao: Union[str, None] = None
    palavraChave1: Union[str, None] = None
    palavraChave2: Union[str, None] = None
    palavraChave3: Union[str, None] = None
    autor: Union[str, None] = None