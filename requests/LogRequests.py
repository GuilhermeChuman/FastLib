from datetime import date
from pydantic import BaseModel

class LogRequests(BaseModel):
    data: date
    idTipoLog: int
    idUsuario: int