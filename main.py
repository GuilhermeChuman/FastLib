from fastapi import FastAPI
from fastapi.responses import RedirectResponse

#Controllers
from controllers.GenerosController import GenerosController
from controllers.EditorasController import EditorasController
from controllers.AutoresController import AutoresController
from controllers.UsuariosController import UsuariosController
from controllers.LivrosController import LivrosController
from controllers.LogsController import LogsController

#Requests
from requests.UsuarioRequests import UsuarioRequests
from requests.GeneroRequests import GeneroRequests
from requests.AutorRequests import AutorRequests

tags_metadata = [
    {
        "name": "Usuários",
        "description": "Rotas relacionadas à listagem e manutenção de usuários",
    },
    {
        "name": "Gêneros",
        "description": "Rotas relacionadas à listagem e manutenção de gêneros literários.",
    },
    {
        "name": "Autores",
        "description": "Rotas relacionadas à listagem e manutenção de autores.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

@app.get("/")
async def standard():
    return RedirectResponse("/docs")

###################################  Usuarios  ########################################

@app.get("/usuarios", tags=["Usuários"], summary="Listar todos os usuários")
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
async def addUsuario(item: GeneroRequests):
    return await GenerosController.addGenero(item.dict())

@app.put("/editGenero/{id}", tags=["Gêneros"])
async def editGenero(id: int, item: GeneroRequests):
    return await GenerosController.editGenero(id, item.dict())

@app.delete("/deleteGenero/{id}", tags=["Gêneros"])
async def deleteGenero(id: int):
    return await GenerosController.deleteGenero(id)

################################   Autores   ##########################################

@app.get("/autores", tags=["Autores"], summary="Listar todos os autores")
async def getAutores():
    return await AutoresController.getAutores()

@app.get("/autores/{id}", tags=["Autores"])
async def getAutorById(id:int):
    return await AutoresController.getAutorById(id)

@app.post("/addAutor", tags=["Autores"])
async def addUsuario(item: AutorRequests):
    return await AutoresController.addAutor(item.dict())

@app.put("/editAutor/{id}", tags=["Autores"])
async def editAutor(id: int, item: AutorRequests):
    return await AutoresController.editAutor(id, item.dict())

@app.delete("/deleteAutor/{id}", tags=["Autores"])
async def deleteAutor(id: int):
    return await AutoresController.deleteAutor(id)

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
