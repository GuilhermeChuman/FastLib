import sys

sys.path.append('../')

from env import DB
from queries.LivrosQueries import LivrosQueries

class LivrosRepository:

    async def getLivros():

        query = LivrosQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        response = []
        for i in rows:
            queryAutor = LivrosQueries.getAutoresByLivro
            autores = await DB.connection.fetch_all(query=queryAutor, values={'id':i['id']})
            response.append({'livro': i, 'autores': autores})
                
        return response

    async def getLivroById(id):

        values = {'id': id}
        query = LivrosQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Livro não encontrada")

        else:
            return rows

    async def addLivro(item):

        query = LivrosQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Livros')

        return data

    async def addLivrosLot(item):

        query = LivrosQueries.add
        await DB.connection.execute_many(query=query, values=item)
        data = []
        data.append(await DB.last_inserted_id('Livros'))

        return data

    async def editLivro(id, item):

        await LivrosRepository.getLivroById(id)

        item['id'] = id
        query = LivrosQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)

        return item

    async def deleteLivro(id):

        await LivrosRepository.getLivroById(id)

        values = {'id': id}
        query = LivrosQueries.delete
        await DB.connection.execute(query=query, values=values)

        return True