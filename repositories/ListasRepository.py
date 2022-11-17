import sys

sys.path.append('../')

from env import DB
from queries.ListasQueries import ListasQueries

class ListasRepository:

    async def verifyLivroNaLista(idLista, idLivro):

        values = {
            'idLista': idLista,
            'idLivro': idLivro
        }

        query = ListasQueries.verifyLivroNaLista
        rows = await DB.connection.fetch_all(query=query, values=values)
        
        if rows == None:
            return False
        else:
            return True

    async def getListaById(idUsuario):

        values = {
            'idUsuario': idUsuario
        }

        query = ListasQueries.getListaById_NumLivros
        rows = await DB.connection.fetch_all(query=query, values=values)
        response = []

        for i in rows:

            obj = {}

            queryLivros = ListasQueries.getListaById
            livros = await DB.connection.fetch_all(query=queryLivros, values={'idLista':i['idLista']})

            obj['idLista']      = i['idLista']
            obj['idUsuario']    = i['idUsuario']
            obj['login']        = i['login']
            obj['total_livros'] = i['total_livros']
            obj['livros']       = livros

            response.append(obj)

        return response

    async def gravaLivroLista(item):

        if(ListasRepository.verifyLivroNaLista(item['idLista'], item['idLivro'])):
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
