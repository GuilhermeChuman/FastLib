import sys

sys.path.append('../')

from repositories.ListasRepository import ListasRepository

class ListasService:

    async def getListaById(idUsuario):

        response = await ListasRepository.getListaById(idUsuario)

        #TRATAMENTOS AQUI

        return response

    async def verifyLivroNaLista(idLista, idLivro):

        response = await ListasRepository.verifyLivroNaLista(idLista, idLivro)

        #TRATAMENTOS AQUI

        return response

    async def getStatus():

        response = await ListasRepository.getStatus()

        #TRATAMENTOS AQUI

        return response

    async def gravaLivroLista(item):

        response = await ListasRepository.gravaLivroLista(item)

        #TRATAMENTOS AQUI

        return response


    async def removeLivroLista(idLista, idLivro):

        response = await ListasRepository.removeLivroLista(idLista, idLivro)

        #TRATAMENTOS AQUI

        return response


    async def getStatussLivroNaLista(idLista, idLivro):

        response = await ListasRepository.getStatussLivroNaLista(idLista, idLivro)

        #TRATAMENTOS AQUI

        return response
    