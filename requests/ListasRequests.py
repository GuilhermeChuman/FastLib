from datetime import date
from pydantic import BaseModel
from typing import Union

class ListasRequests(BaseModel):
    idLista: int
    idLivro: int
    idStatus: int