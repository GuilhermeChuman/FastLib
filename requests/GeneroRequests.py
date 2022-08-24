from pydantic import BaseModel

class GeneroRequests(BaseModel):
    nome: str
    descricao: str