from datetime import date
from pydantic import BaseModel
from typing import Union

class EmprestimosRequests(BaseModel):
    idLivro: int
    idUsuario: int
    dataEmprestimo: Union[date, None] = None
    dataDevolucao: Union[date, None] = None
    estado: str