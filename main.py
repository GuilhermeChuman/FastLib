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
async def deleteUsuario(id:int):
    return await UsuariosController.deleteUsuario(id)

##################################  Generos  ##########################################

@app.get("/generos", tags=["Gêneros"])
async def getGeneros():
    return await GenerosController.getGeneros()

@app.get("/generos/{id}", tags=["Gêneros"])
async def getGeneroById(id:int):
    return await GenerosController.getGeneroById(id)

@app.post("/addGenero", tags=["Gêneros"])
async def addUsuario(item: UsuarioRequests):
    return await GenerosController.addGenero(item.dict())

@app.put("/editGenero/{id}", tags=["Gêneros"])
async def editGenero(id: int, item: UsuarioRequests):
    return await GenerosController.editGenero(id, item.dict())

@app.delete("/deleteGenero/{id}", tags=["Gêneros"])
async def deleteGenero(item: UsuarioRequests):
    return await GenerosController.deleteGenero(item.dict())

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
