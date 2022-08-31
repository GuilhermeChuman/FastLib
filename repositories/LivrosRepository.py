import sys

sys.path.append('../')

from env import DB
from queries.LivrosQueries import LivrosQueries

class LivrosRepository:

    async def getLivros():

        await DB.connection.connect()
        query = LivrosQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        await DB.connection.disconnect()
        
        return rows

    async def getLivroById(id):

        values = {'id': id}
        await DB.connection.connect()
        query = LivrosQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)
        await DB.connection.disconnect()

        if rows == None:
            raise Exception("Livro não encontrada")

        else:
            return rows

    async def addLivro(item):

        await DB.connection.connect()
        query = LivrosQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Livros')
        await DB.connection.disconnect()

        return data

    async def editLivro(id, item):

        await LivrosRepository.getLivroById(id)

        item['id'] = id
        await DB.connection.connect()
        query = LivrosQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        await DB.connection.disconnect()

        return item

    async def deleteLivro(id):

        await LivrosRepository.getLivroById(id)

        values = {'id': id}
        await DB.connection.connect()
        query = LivrosQueries.delete
        await DB.connection.execute(query=query, values=values)
        await DB.connection.disconnect()

        return True