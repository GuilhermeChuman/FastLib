from fastapi import FastAPI, UploadFile
from fastapi.responses import RedirectResponse
from starlette.middleware.cors import CORSMiddleware
from env import DB

#Controllers
from controllers.GenerosController import GenerosController
from controllers.EditorasController import EditorasController
from controllers.AutoresController import AutoresController
from controllers.UsuariosController import UsuariosController
from controllers.LivrosController import LivrosController
from controllers.LogsController import LogsController
from controllers.EmprestimosController import EmprestimosController
from controllers.ListasController import ListasController

#Requests
from requests.UsuarioRequests import UsuarioRequests
from requests.UsuarioRequests import AuthRequests
from requests.UsuarioRequests import SignupRequests

from requests.GeneroRequests import GeneroRequests
from requests.AutorRequests import AutorRequests
from requests.EditoraRequests import EditoraRequests
from requests.LogRequests import LogRequests

from requests.LivroRequests import LivroRequests
from requests.LivroRequests import FilterRequests
from requests.LivroRequests import TrabalhoRequests
from requests.LivroRequests import SolicitarEmprestimoRequests
from requests.LivroRequests import DevolucaoRequests
from requests.ListasRequests import ListasRequests


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
        "name": "Listas",
        "description": "Rotas relacionadas à listagem e manutenção de listas",
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
        {
        "name": "Emprestimos",
        "description": "Rotas relacionadas à empréstimo de livros.",
    },
]

app = FastAPI(openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await DB.connection.connect()

@app.on_event("shutdown")
async def shutdown():
    await DB.connection.disconnect()

@app.get("/")
async def standard():
    return RedirectResponse("/docs")

###################################  Auth  ########################################

@app.post("/auth", tags=["Auth"], summary="")
async def autenticate(item: AuthRequests):
    return await UsuariosController.auth(item.dict())

@app.post("/user/signup", tags=["Auth"], summary="")
async def signup(item: SignupRequests):
    return await UsuariosController.signup(item.dict())

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

@app.post("/addGeneros/lot", tags=["Gêneros"], summary="Recebe  um grupo de gêneros via arquivo .csv")
async def addGenerosLot(file: UploadFile):
    return await GenerosController.addGeneroLot(file)

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

@app.get("/autoresByLivro/{id}", tags=["Autores"], summary="Listar autores por livro")
async def autoresByLivro(id:int):
    return await AutoresController.autoresByLivro(id)

@app.post("/addAutor", tags=["Autores"], summary="Adicionar um novo autor")
async def addUsuario(item: AutorRequests):
    return await AutoresController.addAutor(item.dict())

@app.post("/addAutores/lot", tags=["Autores"], summary="Recebe  um grupo de autores via arquivo .csv")
async def addGenerosLot(file: UploadFile):
    return await AutoresController.addAutoresLot(file)

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

@app.post("/addEditoras/lot", tags=["Editoras"], summary="Recebe  um grupo de editoras via arquivo .csv")
async def addEditorasLot(file: UploadFile):
    return await EditorasController.addEditorasLot(file)

@app.put("/editEditora/{id}", tags=["Editoras"], summary="Editar uma editora")
async def editEditora(id: int, item: EditoraRequests):
    return await EditorasController.editEditora(id, item.dict())

@app.delete("/deleteEditora/{id}", tags=["Editoras"], summary="Deletar uma editora")
async def deleteEditora(id: int):
    return await EditorasController.deleteEditora(id)

##################################    Listas   #############################################

@app.get("/getListaById/{id}", tags=["Listas"], summary="Seleciona a uma lista pelo Id do usuário")
async def getListaById(id: int):
    return await ListasController.getListaById(id)

@app.get("/verifyLivroNaLista/{idLista}/{idLivro}", tags=["Listas"], summary="Seleciona a uma lista pelo Id do usuário")
async def verifyLivroNaLista(idLista, idLivro):
    return await ListasController.verifyLivroNaLista(idLista, idLivro)

@app.get("/getStatusLivroNaLista/{idLista}/{idLivro}", tags=["Listas"], summary="Seleciona a uma lista pelo Id do usuário")
async def getStatussLivroNaLista(idLista, idLivro):
    return await ListasController.getStatussLivroNaLista(idLista, idLivro)

@app.post("/gravaLivroLista", tags=["Listas"], summary="Grava um item novo na lista pelo Id do usuário")
async def gravaLivroLista(item: ListasRequests):
    return await ListasController.gravaLivroLista(item.dict())

@app.get("/removeLivroLista/{idLista}/{idLivro}", tags=["Listas"], summary="Remove um item da lista pelo Id do usuário")
async def removeLivroLista(idLista, idLivro):
    return await ListasController.removeLivroLista(idLista, idLivro)

##################################    Status    #############################################

@app.get("/getStatus", tags=["Status"], summary="Seleciona todos os status")
async def getStatus():
    return await ListasController.getStatus()

###############################    Emprestimos    ##########################################

@app.get("/emprestimo", tags=["Emprestimos"], summary="Apresenta todos os emprestimos ocorridos")
async def getEmprestimos():
    return await EmprestimosController.getEmprestimos()

@app.post("/solicitarEmprestimo", tags=["Emprestimos"], summary="Solicitar emprestimo de um livro")
async def solicitarEmprestimo(item:SolicitarEmprestimoRequests):
    return await LivrosController.solicitarEmprestimo(item.dict())

@app.get("/emprestimosStatus", tags=["Emprestimos"], summary="Apresenta as estatísticas de todos os empréstimos")
async def emprestimosStatus():
    return await EmprestimosController.emprestimosStatus()

@app.get("/aprovarEmprestimo/{id}", tags=["Emprestimos"], summary="Aprovar Empréstimo livro por ID")
async def aprovarEmprestimo(id:int):
    return await LivrosController.aprovarEmprestimo(id)

@app.get("/recusarEmprestimo/{id}", tags=["Emprestimos"], summary="Aprovar Empréstimo livro por ID")
async def recusarEmprestimo(id:int):
    return await LivrosController.recusarEmprestimo(id)

@app.post("/emprestar", tags=["Emprestimos"], summary="Emprestar livro")
async def emprestar(item:SolicitarEmprestimoRequests):
    return await LivrosController.emprestar(item.dict())

@app.post("/devolverLivro", tags=["Emprestimos"], summary="Efetua a devolução de um livro")
async def devolverLivro(item:DevolucaoRequests):
    return await LivrosController.devolverLivro(item.dict())

@app.get("/verifyEmprestimoLivro/{id}", tags=["Emprestimos"], summary="Verifica se o livro está emprestado")
async def verifyEmprestimoLivro(id:int):
    return await LivrosController.verifyEmprestimoLivro(id)

@app.get("/verifySolicitacaoLivro/{idUsuario}/{idLivro}", tags=["Emprestimos"], summary="Verifica se há um empréstimo ativo do usuario para o livro informado")
async def verifySolicitacaoLivro(idUsuario:int, idLivro:int):
    return await LivrosController.verifySolicitacaoLivro(idUsuario, idLivro)

###############################    Livros    ##########################################

@app.get("/livros", tags=["Livros"], summary="Listar todos os livros")
async def getLivros():
    return await LivrosController.getLivros()

@app.get("/allLivrosStatus", tags=["Livros"], summary="Informa as estatísticas do acerto da biblioteca")
async def allLivrosStatus():
    return await LivrosController.allLivrosStatus()

@app.get("/getLivrosSemEmprestimo", tags=["Livros"], summary="Listar todos os livros que não possuem empréstimo")
async def getLivrosSemEmprestimo():
    return await LivrosController.getLivrosSemEmprestimo()

@app.get("/livros/{id}", tags=["Livros"], summary="Listar um Livro por ID")
async def getLivroById(id:int):
    return await LivrosController.getLivroById(id)

@app.post("/addTrabalho", tags=["Livros"], summary="Adicionar um novo Autor à um livro existente")
async def addTrabalho(item: TrabalhoRequests):
    return await LivrosController.addTrabalho(item.dict())

@app.delete("/removeTrabalho/{id}", tags=["Livros"], summary="Remove um Autor de um livro existente")
async def removeTrabalho(id: int):
    return await LivrosController.removeTrabalho(id)

@app.post("/livros/{id}", tags=["Livros"], summary="Listar livros através de filtro")
async def filterLivros(item: FilterRequests, id: int):
    return await LivrosController.filterLivros(item.dict(), id)

@app.post("/addLivros/lot", tags=["Livros"], summary="Recebe  um grupo de livros via arquivo .csv")
async def addLivrosLot(file: UploadFile):
    return await LivrosController.addLivrosLot(file)

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