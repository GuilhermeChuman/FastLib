import sys

sys.path.append('../')

from env import DB
from queries.AutoresQueries import AutoresQueries

class AutoresRepository:

    async def getAutores():

        await DB.connection.connect()
        query = AutoresQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        await DB.connection.disconnect()
        
        return rows

    async def getAutorById(id):

        values = {'id': id}
        await DB.connection.connect()
        query = AutoresQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)
        await DB.connection.disconnect()

        if rows == None:
            raise Exception("Autor não encontrado")

        else:
            return rows

    async def addAutor(item):

        await DB.connection.connect()
        query = AutoresQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Autores')
        await DB.connection.disconnect()

        return data

    async def addAutoresLot(item):

        await DB.connection.connect()
        query = AutoresQueries.add
        await DB.connection.execute_many(query=query, values=item)
        data = []
        data.append(await DB.last_inserted_id('Autores'))
        await DB.connection.disconnect()

        return data

    async def editAutor(id, item):

        await AutoresRepository.getAutorById(id)

        item['id'] = id
        await DB.connection.connect()
        query = AutoresQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        await DB.connection.disconnect()

        return item

    async def deleteAutor(id):

        await AutoresRepository.getAutorById(id)

        values = {'id': id}
        await DB.connection.connect()
        query = AutoresQueries.delete
        await DB.connection.execute(query=query, values=values)
        await DB.connection.disconnect()

        return True