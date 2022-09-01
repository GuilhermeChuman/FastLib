import sys

sys.path.append('../')

from env import DB
from queries.EditorasQueries import EditorasQueries

class EditorasRepository:

    async def getEditoras():

        query = EditorasQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        
        return rows

    async def getEditoraById(id):

        values = {'id': id}
        query = EditorasQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Editora não encontrada")

        else:
            return rows

    async def addEditora(item):

        query = EditorasQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Editoras')

        return data

    async def addEditorasLot(item):

        query = EditorasQueries.add
        await DB.connection.execute_many(query=query, values=item)
        data = []
        data.append(await DB.last_inserted_id('Editoras'))

        return data

    async def editEditora(id, item):

        await EditorasRepository.getEditoraById(id)

        item['id'] = id
        query = EditorasQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)

        return item

    async def deleteEditora(id):

        await EditorasRepository.getEditoraById(id)

        values = {'id': id}
        query = EditorasQueries.delete
        await DB.connection.execute(query=query, values=values)

        return True