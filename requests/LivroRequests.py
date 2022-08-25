from datetime import date
from pydantic import BaseModel

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