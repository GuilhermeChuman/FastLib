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

    async def allLivrosStatus():
        
        query = LivrosQueries.totalLivros
        totalLivros = await DB.connection.fetch_one(query=query)

        query = LivrosQueries.totalEmprestados
        totalEmprestados = await DB.connection.fetch_one(query=query)

        query = LivrosQueries.emprestimosPorLivro
        emprestimosPorLivro = await DB.connection.fetch_all(query=query)

        query = LivrosQueries.emprestimosPorGenero
        emprestimosPorGenero = await DB.connection.fetch_all(query=query)

        query = LivrosQueries.livrosPorGenero
        livrosPorGenero = await DB.connection.fetch_all(query=query)

        obj = {}
        obj['total'] = totalLivros['total']
        obj['emprestados'] = totalEmprestados['total']
        obj['disponiveis'] = totalLivros['total'] - totalEmprestados['total']
        obj['livrosPorGenero'] = livrosPorGenero
        obj['emprestimosPorLivro'] = emprestimosPorLivro
        obj['emprestimosPorGenero'] = emprestimosPorGenero

        return obj

    async def getLivrosSemEmprestimo():

        query = LivrosQueries.getAllSemEmprestimo
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

    async def solicitarEmprestimo(item):

        values = item
        query = LivrosQueries.solicitarEmprestimo
        await DB.connection.execute(query=query, values=values)

        return True

    async def aprovarEmprestimo(id):

        emprestimo = await LivrosRepository.findEmprestimoById(id)

        if(await LivrosRepository.verifyEmprestimoLivro(emprestimo['idLivro'])):
            raise Exception('O livro já está emprestado!')

        values = {'id': id}
        query = LivrosQueries.aprovarEmprestimo
        await DB.connection.execute(query=query, values=values)

        return True

    async def recusarEmprestimo(id):

        emprestimo = await LivrosRepository.findEmprestimoById(id)

        values = {'id': id}
        query = LivrosQueries.recusarEmprestimo
        await DB.connection.execute(query=query, values=values)

        return True

    async def emprestar(item):

        values = item
        query = LivrosQueries.emprestar
        await DB.connection.execute(query=query, values=values)

        return True

    async def devolverLivro(item):

        values = item

        query = LivrosQueries.devolverLivro
        await DB.connection.execute(query=query, values=values)

        return True

    async def verifyEmprestimoLivro(id):

        values = {'id': id}
        query = LivrosQueries.verifyEmprestimoLivro
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            return False
        else:
            return True

    async def verifySolicitacaoLivro(idUsuario, idLivro):

        values = {'idUsuario': idUsuario, 'idLivro': idLivro}
        query = LivrosQueries.verifySolicitacaoLivro
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            return False
        else:
            return True

    async def findEmprestimoById(id):

        values = {'id': id}
        query = LivrosQueries.getEmprestimoById
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Emprestimo não encontrado")

        else:
            return rows

    async def removeTrabalho(id):

        await LivrosRepository.getTrabalhoById(id)

        values = {'id': id}
        query = LivrosQueries.removeTrabalho
        await DB.connection.execute(query=query, values=values)

        return True

    async def getLivrosOnList(id):

        values = {'id': id}
        query = LivrosQueries.getLivrosOnList
        print(query)
        response = await DB.connection.fetch_all(query=query, values=values)

        return response

    async def getLivroById(id):

        values = {'id': id}
        query = LivrosQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)

        queryAutor = LivrosQueries.getAutoresByLivro
        autores = await DB.connection.fetch_all(query=queryAutor, values={'id':id})
        
        obj = {}

        obj['id']               = rows['id']
        obj['isbn']             = rows['isbn']
        obj['titulo']           = rows['titulo']
        obj['descricao']        = rows['descricao']
        obj['volume']           = rows['volume']
        obj['palavraChave1']    = rows['palavraChave1']
        obj['palavraChave2']    = rows['palavraChave2']
        obj['palavraChave3']    = rows['palavraChave3']
        obj['ano']              = rows['ano']
        obj['edicao']           = rows['edicao']
        obj['idEditora']        = rows['idEditora']
        obj['editora']          = rows['editora']
        obj['idGenero']         = rows['idGenero']
        obj['genero']           = rows['genero']
        obj['autores']          = autores
            
        if rows == None:
            raise Exception("Livro não encontrado")

        else:
            return obj

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