import sys

sys.path.append('../')

from env import DB
from queries.ListasQueries import ListasQueries

class ListasRepository:

    async def verifyLivroNaLista(idUsuario, idLivro):

        values = {
            'idUsuario': idUsuario,
            'idLivro': idLivro
        }

        query = ListasQueries.verifyLivroNaLista
        rows = await DB.connection.fetch_all(query=query, values=values)
        
        if rows == None:
            return False
        else:
            return True

    async def getStatus():
        
        query = ListasQueries.getStatus
        rows = await DB.connection.fetch_all(query=query)
        
        return rows

    async def getListaById(idUsuario):

        values = {
            'idUsuario': idUsuario
        }

        query = ListasQueries.getListaById_NumLivros
        lista = await DB.connection.fetch_one(query=query, values=values)

        obj = {}

        queryLivros = ListasQueries.getListaById
        livros = await DB.connection.fetch_all(query=queryLivros, values={'idLista':lista['idLista']})

        obj['idLista']      = lista.idLista
        obj['idUsuario']    = lista.idUsuario
        obj['login']        = lista.login
        obj['total_livros'] = lista.total_livros
        obj['livros']       = livros

        return obj

    async def gravaLivroLista(item):

        if(ListasRepository.verifyLivroNaLista(item['idUsuario'], item['idLivro'])):
            return ListasRepository.insertLivroLista(item)
        else:
            return ListasRepository.updateLivroLista(item)


    async def insertLivroLista(item):

        values = item
        query = ListasQueries.insertLivroLista
        await DB.connection.execute(query=query, values=values)

        return True

    async def updateLivroLista(item):

        values = item
        query = ListasQueries.updateLivroLista
        await DB.connection.execute(query=query, values=values)

        return True

    async def removeLivroLista(idLista):

        values = {'idLista': idLista}
        query = ListasQueries.removeLivroLista
        await DB.connection.execute(query=query, values=values)

        return True
