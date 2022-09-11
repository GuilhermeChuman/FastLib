from datetime import date
from pydantic import BaseModel
from typing import Union

class LivroRequests(BaseModel):
    isbn: Union[str, None] = None
    titulo: str
    descricao:  Union[str, None] = None
    volume:  Union[str, None] = None
    palavraChave1: Union[str, None] = None
    palavraChave2: Union[str, None] = None
    palavraChave3: Union[str, None] = None
    ano: Union[str, None] = None
    edicao: Union[str, None] = None
    idEditora: Union[int, None] = None
    idGenero: Union[int, None] = None

class TrabalhoRequests(BaseModel):
    idAutor: int
    idLivro: int

class SolicitarEmprestimoRequests(BaseModel):
    idUsuario: int
    idLivro: int
    dataEmprestimo: date

class FilterRequests(BaseModel):
    titulo: Union[str, None] = None
    descricao: Union[str, None] = None
    palavraChave1: Union[str, None] = None
    palavraChave2: Union[str, None] = None
    palavraChave3: Union[str, None] = None
    autores: Union[str, None] = None