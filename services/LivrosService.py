import sys

sys.path.append('../')

from repositories.LivrosRepository import LivrosRepository

class LivrosService:

    async def getLivros():

        response = await LivrosRepository.getLivros()

        #TRATAMENTOS AQUI

        return response

    async def getLivroById(id):

        response = await LivrosRepository.getLivroById(id)

        #TRATAMENTOS AQUI

        return response

    async def filterLivros(item):

        response = await LivrosRepository.getLivros()

        expectedResult = [d for d in response if d['titulo'] in item['titulo']]
    
        if(len(expectedResult) == 0):
            raise Exception("Livro não encontrado")

        return expectedResult

    async def addLivro(item):

        response = await LivrosRepository.addLivro(item)

        #TRATAMENTOS AQUI

        return response

    async def editLivro(id, item):

        response = await LivrosRepository.editLivro(id, item)

        #TRATAMENTOS AQUI

        return response

    async def deleteLivro(id):

        response = await LivrosRepository.deleteLivro(id)

        #TRATAMENTOS AQUI

        return response