import sys

sys.path.append('../')

from env import DB
from queries.AutoresQueries import AutoresQueries

class AutoresRepository:

    async def getAutores():

        query = AutoresQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        
        return rows

    async def autoresByLivro(id):

        query = AutoresQueries.getAutoresByLivro
        rows = await DB.connection.fetch_all(query=query, values={"id": id})

        return rows

    async def getAutorById(id):

        values = {'id': id}
        query = AutoresQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Autor não encontrado")

        else:
            return rows

    async def addAutor(item):

        query = AutoresQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Autores')

        return data

    async def addAutoresLot(item):

        query = AutoresQueries.add
        await DB.connection.execute_many(query=query, values=item)
        data = []
        data.append(await DB.last_inserted_id('Autores'))

        return data

    async def editAutor(id, item):

        await AutoresRepository.getAutorById(id)

        item['id'] = id
        query = AutoresQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)

        return item

    async def deleteAutor(id):

        await AutoresRepository.getAutorById(id)

        values = {'id': id}
        query = AutoresQueries.delete
        await DB.connection.execute(query=query, values=values)

        return True