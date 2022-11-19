import sys

sys.path.append('../')

from env import DB
from queries.ListasQueries import ListasQueries

class ListasRepository:

    async def getStatussLivroNaLista(idLista, idLivro):

        values = {
            'idLista': idLista,
            'idLivro': idLivro
        }

        if(await ListasRepository.verifyLivroNaLista(idLista, idLivro)):
            query = ListasQueries.getStatussLivroNaLista
            rows = await DB.connection.fetch_one(query=query, values=values)
        
            return rows.idStatus

    async def verifyLivroNaLista(idLista, idLivro):

        values = {
            'idLista': idLista,
            'idLivro': idLivro
        }

        query = ListasQueries.verifyLivroNaLista
        rows = await DB.connection.fetch_all(query=query, values=values)
        
        if len(rows) == 0:
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

        if(await ListasRepository.verifyLivroNaLista(item['idLista'], item['idLivro'])):
            return await ListasRepository.updateLivroLista(item)
        else:
            return await ListasRepository.insertLivroLista(item)


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

    async def removeLivroLista(idLista, idLivro):

        values = {'idLista': idLista, 'idLivro': idLivro}
        query = ListasQueries.removeLivroLista
        await DB.connection.execute(query=query, values=values)

        return True
