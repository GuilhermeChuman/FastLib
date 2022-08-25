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
from requests.UsuarioRequests import AuthRequests

from requests.GeneroRequests import GeneroRequests
from requests.AutorRequests import AutorRequests
from requests.EditoraRequests import EditoraRequests
from requests.LogRequests import LogRequests

from requests.LivroRequests import LivroRequests
from requests.LivroRequests import FilterRequests

tags_metadata = [
    {
        "name": "Auth",
        "description": "Rotas relacionadas à autenticação",
    },
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
    {
        "name": "Editoras",
        "description": "Rotas relacionadas à listagem e manutenção de editoras.",
    },
    {
        "name": "Logs",
        "description": "Rotas relacionadas à listagem e manutenção de logs.",
    },
    {
        "name": "Livros",
        "description": "Rotas relacionadas à listagem e manutenção de livros.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

@app.get("/")
async def standard():
    return RedirectResponse("/docs")

###################################  Auth  ########################################

@app.post("/auth", tags=["Auth"], summary="")
async def autenticate(item: AuthRequests):
    return await UsuariosController.auth(item.dict())

###################################  Usuarios  ########################################

@app.get("/usuarios", tags=["Usuários"], summary="Listar todos os usuários")
async def getUsuarios():
    return await UsuariosController.getUsuarios()

@app.get("/usuarios/{id}", tags=["Usuários"], summary="Listar um usuário pelo ID")
async def getUsuarioById(id:int):
    return await UsuariosController.getUsuarioById(id)

@app.post("/addUsuario", tags=["Usuários"], summary="Adicionar um novo usuário")
async def addUsuario(item: UsuarioRequests):
    return await UsuariosController.addUsuario(item.dict())

@app.put("/editUsuario/{id}", tags=["Usuários"], summary="Editar um usuário")
async def editUsuario(id: int, item: UsuarioRequests):
    return await UsuariosController.editUsuario(id, item.dict())

@app.delete("/deleteUsuario/{id}", tags=["Usuários"], summary="Deletar um usuário")
async def deleteUsuario(id:int):
    return await UsuariosController.deleteUsuario(id)

##################################  Generos  ##########################################

@app.get("/generos", tags=["Gêneros"], summary="Listar todos os gêneros")
async def getGeneros():
    return await GenerosController.getGeneros()

@app.get("/generos/{id}", tags=["Gêneros"], summary="Listar um gênero por ID")
async def getGeneroById(id:int):
    return await GenerosController.getGeneroById(id)

@app.post("/addGenero", tags=["Gêneros"], summary="Adicionar um novo gêneros")
async def addUsuario(item: GeneroRequests):
    return await GenerosController.addGenero(item.dict())

@app.put("/editGenero/{id}", tags=["Gêneros"], summary="Editar um gênero")
async def editGenero(id: int, item: GeneroRequests):
    return await GenerosController.editGenero(id, item.dict())

@app.delete("/deleteGenero/{id}", tags=["Gêneros"], summary="Deletar um gênero")
async def deleteGenero(id: int):
    return await GenerosController.deleteGenero(id)

################################   Autores   ##########################################

@app.get("/autores", tags=["Autores"], summary="Listar todos os autores")
async def getAutores():
    return await AutoresController.getAutores()

@app.get("/autores/{id}", tags=["Autores"], summary="Listar um autor por ID")
async def getAutorById(id:int):
    return await AutoresController.getAutorById(id)

@app.post("/addAutor", tags=["Autores"], summary="Adicionar um novo autor")
async def addUsuario(item: AutorRequests):
    return await AutoresController.addAutor(item.dict())

@app.put("/editAutor/{id}", tags=["Autores"], summary="Editar um autor")
async def editAutor(id: int, item: AutorRequests):
    return await AutoresController.editAutor(id, item.dict())

@app.delete("/deleteAutor/{id}", tags=["Autores"], summary="Deletar um autor")
async def deleteAutor(id: int):
    return await AutoresController.deleteAutor(id)

###############################   Editoras   ##########################################

@app.get("/editoras", tags=["Editoras"], summary="Listar todas as editoras")
async def getEditoras():
    return await EditorasController.getEditoras()

@app.get("/editoras/{id}", tags=["Editoras"], summary="Listar um editora por ID")
async def getEditoraById(id:int):
    return await EditorasController.getEditoraById(id)

@app.post("/addEditora", tags=["Editoras"], summary="Adicionar uma nova editora")
async def addEditora(item: EditoraRequests):
    return await EditorasController.addEditora(item.dict())

@app.put("/editEditora/{id}", tags=["Editoras"], summary="Editar uma editora")
async def editEditora(id: int, item: EditoraRequests):
    return await EditorasController.editEditora(id, item.dict())

@app.delete("/deleteEditora/{id}", tags=["Editoras"], summary="Deletar uma editora")
async def deleteEditora(id: int):
    return await EditorasController.deleteEditora(id)

###############################    Livros    ##########################################

@app.get("/livros", tags=["Livros"], summary="Listar todos os livros")
async def getLivros():
    return await LivrosController.getLivros()

@app.get("/livros/{id}", tags=["Livros"], summary="Listar um Livro por ID")
async def getLivroById(id:int):
    return await LivrosController.getLivroById(id)

@app.post("/livros/", tags=["Livros"], summary="Listar livros através de filtro")
async def filterLivros(item: FilterRequests):
    return await LivrosController.filterLivros(item.dict())

@app.post("/addLivro", tags=["Livros"], summary="Adicionar um novo Livro")
async def addLivro(item: LivroRequests):
    return await LivrosController.addLivro(item.dict())

@app.put("/editLivro/{id}", tags=["Livros"], summary="Editar um Livro")
async def editLivro(id: int, item: LivroRequests):
    return await LivrosController.editLivro(id, item.dict())

@app.delete("/deleteLivro/{id}", tags=["Livros"], summary="Deletar um Livro")
async def deleteLivro(id: int):
    return await LivrosController.deleteLivro(id)

###############################     Logs    ##########################################

@app.get("/logs", tags=["Logs"], summary="Listar todas os logs")
async def getLivros():
    return await LogsController.getLogs()

@app.get("/logs/{id}", tags=["Logs"], summary="Listar um log por ID")
async def getLogById(id:int):
    return await LogsController.getLogById(id)

@app.post("/addLog", tags=["Logs"], summary="Adicionar um novo log")
async def addLog(item: LogRequests):
    return await LogsController.addLog(item.dict())