from pydantic import BaseModel
from typing import Union

class UsuarioRequests(BaseModel):
    login: str
    password: str
    nome: str
    email: str
    validationToken: Union[str, None] = None
    status: str

class AuthRequests(BaseModel):
    login: str
    password: str

class SignupRequests(BaseModel):
    nome: str
    email: str
    login: str
    password: str
    
