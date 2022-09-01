import sys

sys.path.append('../')

from env import DB
from queries.GenerosQueries import GenerosQueries

class GenerosRepository:

    async def getGeneros():

        query = GenerosQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        
        return rows

    async def getGeneroById(id):

        values = {'id': id}
        query = GenerosQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Gênero não encontrado")

        else:
            return rows

    async def addGenero(item):

        query = GenerosQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Generos')

        return data

    async def addGeneroLot(item):

        query = GenerosQueries.add
        await DB.connection.execute_many(query=query, values=item)
        data = []
        data.append(await DB.last_inserted_id('Generos'))

        return data

    async def editGenero(id, item):

        await GenerosRepository.getGeneroById(id)

        item['id'] = id
        query = GenerosQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)

        return item

    async def deleteGenero(id):

        await GenerosRepository.getGeneroById(id)

        values = {'id': id}
        query = GenerosQueries.delete
        await DB.connection.execute(query=query, values=values)

        return True