from pydantic import BaseModel
from typing import Union

from enum import Enum
 
class UsuarioRequests(BaseModel):
    login: str
    password: str
    nome: str
    email: str
    validationToken: Union[str, None] = None
    status: str