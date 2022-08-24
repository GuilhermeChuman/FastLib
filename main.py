from fastapi import FastAPI

#Controllers
from controllers.GenerosController import GenerosController
from controllers.EditorasController import EditorasController
from controllers.AutoresController import AutoresController
from controllers.UsuariosController import UsuariosController
from controllers.LivrosController import LivrosController
from controllers.LogsController import LogsController

#Requests
from requests.UsuarioRequests import UsuarioRequests

tags_metadata = [
    {
        "name": "Usuários",
        "description": "Rotas relacionadas à listagem e manutenção de usuários",
    },
    {
        "name": "Gêneros",
        "description": "Rotas relacionadas à listagem e manutenção de gêneros literários.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

###################################  Usuarios  ########################################

@app.get("/usuarios", tags=["Usuários"])
async def getUsuarios():
    return await UsuariosController.getUsuarios()

@app.get("/usuarios/{id}", tags=["Usuários"])
async def getUsuarioById(id:int):
    return await UsuariosController.getUsuarioById(id)

@app.post("/addUsuario", tags=["Usuários"])
async def addUsuario(item: UsuarioRequests):
    return await UsuariosController.addUsuario(item.dict())

@app.put("/editUsuario/{id}", tags=["Usuários"])
async def editUsuario(id: int, item: UsuarioRequests):
    return await UsuariosController.editUsuario(id, item.dict())

@app.delete("/deleteUsuario/{id}", tags=["Usuários"])
async def editUsuario(item: UsuarioRequests):
    return await UsuariosController.editUsuario(item.dict())

##################################  Generos  ##########################################

@app.get("/generos", tags=["Gêneros"])
async def getGeneros():
    return await GenerosController.getGeneros()

################################   Autores   ##########################################

@app.get("/autores")
async def getAutores():
    return await AutoresController.getAutores()

###############################   Editoras   ##########################################

@app.get("/editoras")
async def getEditoras():
    return await EditorasController.getEditoras()

###############################    Livros    ##########################################

@app.get("/livros")
async def getLivros():
    return await LivrosController.getLivros()

###############################     Logs    ##########################################

@app.get("/logs")
async def getLivros():
    return await LogsController.getLogs()
