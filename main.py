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

app = FastAPI()

###################################  Usuarios  ########################################

@app.get("/usuarios")
async def getUsuarios():
    return await UsuariosController.getUsuarios()

@app.post("/addUsuario")
async def addUsuario(item: UsuarioRequests):
    return await UsuariosController.addUsuario(item.dict())

##################################  Generos  ##########################################

@app.get("/generos")
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
