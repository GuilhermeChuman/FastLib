import sys

sys.path.append('../')

from env import DB
from queries.GenerosQueries import GenerosQueries

class GenerosRepository:

    async def getGeneros():

        await DB.connection.connect()
        query = GenerosQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        await DB.connection.disconnect()
        
        return rows

    async def getGeneroById(id):

        values = {'id': id}
        await DB.connection.connect()
        query = GenerosQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)
        await DB.connection.disconnect()

        if rows == None:
            raise Exception("Gênero não encontrado")

        else:
            return rows

    async def addGenero(item):

        await DB.connection.connect()
        query = GenerosQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Generos')
        await DB.connection.disconnect()

        return data

    async def editGenero(id, item):

        await GenerosRepository.getGeneroById(id)

        item['id'] = id
        await DB.connection.connect()
        query = GenerosQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        await DB.connection.disconnect()

        return item

    async def deleteGenero(id):

        await GenerosRepository.getGeneroById(id)

        values = {'id': id}
        await DB.connection.connect()
        query = GenerosQueries.delete
        await DB.connection.execute(query=query, values=values)
        await DB.connection.disconnect()

        return None