import sys
import pandas as pd
import ast
from itertools import groupby
from operator import itemgetter
from fuzzywuzzy import fuzz
import yake

sys.path.append('../')

from env import CsvReader
from repositories.LivrosRepository import LivrosRepository

class LivrosService:

    async def getLivros():

        response = await LivrosRepository.getLivros()

        #TRATAMENTOS AQUI

        return response

    async def allLivrosStatus():

        response = await LivrosRepository.allLivrosStatus()

        #TRATAMENTOS AQUI

        return response

    async def getLivrosSemEmprestimo():

        response = await LivrosRepository.getLivrosSemEmprestimo()

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

    async def recusarEmprestimo(id):

        response = await LivrosRepository.recusarEmprestimo(id)

        #TRATAMENTOS AQUI

        return response

    async def emprestar(item):

        response = await LivrosRepository.emprestar(item)

        #TRATAMENTOS AQUI

        return response

    async def devolverLivro(item):

        response = await LivrosRepository.devolverLivro(item)

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

    async def constructObjLivro(livro, ratio):

        obj = {}
        obj['id']               = livro['id']
        obj['isbn']             = livro['isbn']
        obj['titulo']           = livro['titulo']
        obj['descricao']        = livro['descricao']
        obj['volume']           = livro['volume']
        obj['palavraChave1']    = livro['palavraChave1']
        obj['palavraChave2']    = livro['palavraChave2']
        obj['palavraChave3']    = livro['palavraChave3']
        obj['ano']              = livro['ano']
        obj['edicao']           = livro['edicao']
        obj['idEditora']        = livro['idEditora']
        obj['editora']          = livro['editora']
        obj['idGenero']         = livro['idGenero']
        obj['genero']           = livro['genero']
        obj['status']           = livro['status']
        obj['cor']              = livro['cor']
        obj['autores']          = livro['autores']
        obj['ratio']            = ratio

        return obj

    async def filterLivros(item, id):

        responsePrimary = await LivrosRepository.getLivros()

        response = []

        for livro in responsePrimary:

            ratioTitulo =  fuzz.ratio(livro['titulo'], item['titulo'])/3
            ratioTitulo += fuzz.partial_ratio(livro['titulo'], item['titulo'])/3
            ratioTitulo += fuzz.token_sort_ratio(livro['titulo'], item['titulo'])/3

            ratioDescricao =  fuzz.ratio(livro['descricao'], item['descricao'])/3
            ratioDescricao += fuzz.partial_ratio(livro['descricao'], item['descricao'])/3
            ratioDescricao += fuzz.token_sort_ratio(livro['descricao'], item['descricao'])/3

            ratioPalavraChave1 =  fuzz.ratio(livro['palavraChave1'], item['palavraChave1'])/3
            ratioPalavraChave1 += fuzz.partial_ratio(livro['palavraChave1'], item['palavraChave1'])/3
            ratioPalavraChave1 += fuzz.token_sort_ratio(livro['palavraChave1'], item['palavraChave1'])/3

            ratioPalavraChave2 =  fuzz.ratio(livro['palavraChave2'], item['palavraChave2'])/3
            ratioPalavraChave2 += fuzz.partial_ratio(livro['palavraChave2'], item['palavraChave2'])/3
            ratioPalavraChave2 += fuzz.token_sort_ratio(livro['palavraChave2'], item['palavraChave2'])/3

            ratioPalavraChave3 =  fuzz.ratio(livro['palavraChave3'], item['palavraChave3'])/3
            ratioPalavraChave3 += fuzz.partial_ratio(livro['palavraChave3'], item['palavraChave3'])/3
            ratioPalavraChave3 += fuzz.token_sort_ratio(livro['palavraChave3'], item['palavraChave3'])/3

            ratioAutores =  fuzz.ratio(livro['autores'], item['autores'])/3
            ratioAutores += fuzz.partial_ratio(livro['autores'], item['autores'])/3
            ratioAutores += fuzz.token_sort_ratio(livro['autores'], item['autores'])/3

            if(ratioTitulo > 60):
                response.append(await LivrosService.constructObjLivro(livro, ratioTitulo))
            elif(ratioDescricao > 60):
                response.append(await LivrosService.constructObjLivro(livro, ratioDescricao))
            elif(ratioPalavraChave1 > 60):
                response.append(await LivrosService.constructObjLivro(livro, ratioPalavraChave1))
            elif(ratioPalavraChave2 > 60):
                response.append(await LivrosService.constructObjLivro(livro, ratioPalavraChave2))
            elif(ratioPalavraChave3 > 60):
                response.append(await LivrosService.constructObjLivro(livro, ratioPalavraChave3))
            elif(ratioAutores > 60):    
                response.append(await LivrosService.constructObjLivro(livro, ratioAutores))

        newRows = sorted(response, key = itemgetter('ratio'))
        newRows = newRows[::-1]

        return newRows

    async def addLivro(item):

        kw_extractor = yake.KeywordExtractor()
        text = item['descricao']
        language = "pt"
        max_ngram_size = 3
        deduplication_threshold = 0.9
        numOfKeywords = 30
        custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

        palavra_chave = custom_kw_extractor.extract_keywords(text)

        for kw in palavra_chave:
            print(kw)

        return None
        
        #if(item['palavraChave1'] == None or  item['palavraChave1'] == ''):

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