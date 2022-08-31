import sys

sys.path.append('../')

from env import DB
from queries.EditorasQueries import EditorasQueries

class EditorasRepository:

    async def getEditoras():

        await DB.connection.connect()
        query = EditorasQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        await DB.connection.disconnect()
        
        return rows

    async def getEditoraById(id):

        values = {'id': id}
        await DB.connection.connect()
        query = EditorasQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)
        await DB.connection.disconnect()

        if rows == None:
            raise Exception("Editora não encontrada")

        else:
            return rows

    async def addEditora(item):

        await DB.connection.connect()
        query = EditorasQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Editoras')
        await DB.connection.disconnect()

        return data

    async def addEditorasLot(item):

        await DB.connection.connect()
        query = EditorasQueries.add
        await DB.connection.execute_many(query=query, values=item)
        data = []
        data.append(await DB.last_inserted_id('Editoras'))
        await DB.connection.disconnect()

        return data

    async def editEditora(id, item):

        await EditorasRepository.getEditoraById(id)

        item['id'] = id
        await DB.connection.connect()
        query = EditorasQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        await DB.connection.disconnect()

        return item

    async def deleteEditora(id):

        await EditorasRepository.getEditoraById(id)

        values = {'id': id}
        await DB.connection.connect()
        query = EditorasQueries.delete
        await DB.connection.execute(query=query, values=values)
        await DB.connection.disconnect()

        return None