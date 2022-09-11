import sys
import pandas as pd
import ast


sys.path.append('../')

from env import CsvReader
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

    async def solicitarEmprestimo(item):

        response = await LivrosRepository.solicitarEmprestimo(item)

        #TRATAMENTOS AQUI

        return response

    async def aprovarEmprestimo(id):

        response = await LivrosRepository.aprovarEmprestimo(id)

        #TRATAMENTOS AQUI

        return response

    async def emprestar(item):

        response = await LivrosRepository.emprestar(item)

        #TRATAMENTOS AQUI

        return response

    async def devolverLivro(id):

        response = await LivrosRepository.devolverLivro(id)

        #TRATAMENTOS AQUI

        return response

        
    async def verifyEmprestimoLivro(id):

        response = await LivrosRepository.verifyEmprestimoLivro(id)

        #TRATAMENTOS AQUI

        return response


    async def addTrabalho(item):

        response = await LivrosRepository.addTrabalho(item)

        return response

    async def removeTrabalho(id):

        response = await LivrosRepository.removeTrabalho(id)

        return response

    async def filterLivros(item, id):

        responsePrimary = await LivrosRepository.getLivros()
            
        df = pd.DataFrame(responsePrimary)
        df = df.fillna('')

        response = []
        finalResponse = []

        for x, y in item.items():
            if(y != None):
                arrayTitulo = df.query(x+".str.contains('"+y+"', na=False, case=False)")
                arrayTitulo = arrayTitulo.to_dict('index')
                response.append([value for value in arrayTitulo.values()])

        response.append(await LivrosRepository.getLivrosOnList(id))

        finalResponse = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in response])]
        
        if len(finalResponse) == 0:
            return responsePrimary

        return finalResponse

    async def addLivro(item):

        response = await LivrosRepository.addLivro(item)

        #TRATAMENTOS AQUI

        return response

    async def addLivrosLot(item):

        data = await CsvReader.readFile(item) 
        response = await LivrosRepository.addLivrosLot(data)
        return response

    async def editLivro(id, item):

        response = await LivrosRepository.editLivro(id, item)

        #TRATAMENTOS AQUI

        return response

    async def deleteLivro(id):

        response = await LivrosRepository.deleteLivro(id)

        #TRATAMENTOS AQUI

        return response