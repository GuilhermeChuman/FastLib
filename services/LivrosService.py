import sys
import pandas as pd
import ast
from fuzzywuzzy import fuzz


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

    async def verifySolicitacaoLivro(idUsuario, idLivro):

        response = await LivrosRepository.verifySolicitacaoLivro(idUsuario, idLivro)

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

        response = []

        for livro in responsePrimary:
            
            if(fuzz.partial_ratio(livro['titulo'], item['titulo']) > 70):
                response.append(livro)
            elif(fuzz.partial_ratio(livro['descricao'], item['descricao']) > 70):
                response.append(livro)
            elif(fuzz.partial_ratio(livro['palavraChave1'], item['palavraChave1']) > 70):
                response.append(livro)
            elif(fuzz.partial_ratio(livro['palavraChave2'], item['palavraChave2']) > 70):
                response.append(livro)
            elif(fuzz.partial_ratio(livro['palavraChave3'], item['palavraChave3']) > 70):
                response.append(livro)
            elif(fuzz.partial_ratio(livro['autores'], item['autores']) > 70):    
                response.append(livro)

        return response

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