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

            obj = {}

            queryAutor = LivrosQueries.getAutoresByLivro
            autores = await DB.connection.fetch_all(query=queryAutor, values={'id':i['id']})
            
            obj['id']               = i['id']
            obj['isbn']             = i['isbn']
            obj['titulo']           = i['titulo']
            obj['descricao']        = i['descricao']
            obj['volume']           = i['volume']
            obj['palavraChave1']    = i['palavraChave1']
            obj['palavraChave2']    = i['palavraChave2']
            obj['palavraChave3']    = i['palavraChave3']
            obj['ano']              = i['ano']
            obj['edicao']           = i['edicao']
            obj['idEditora']        = i['idEditora']
            obj['editora']          = i['editora']
            obj['idGenero']         = i['idGenero']
            obj['genero']           = i['genero']
            obj['autores']          = autores
                
            response.append(obj)
                
        return response

    async def addTrabalho(item):

        query = LivrosQueries.addTrabalho
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Trabalhos')

        return data

    async def getTrabalhoById(id):

        values = {'id': id}
        query = LivrosQueries.getTrabalhoById
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Trabalho não encontrado")

        else:
            return rows

    async def removeTrabalho(id):

        await LivrosRepository.getTrabalhoById(id)

        values = {'id': id}
        query = LivrosQueries.removeTrabalho
        await DB.connection.execute(query=query, values=values)

        return True


    async def getLivroById(id):

        values = {'id': id}
        query = LivrosQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Livro não encontrado")

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