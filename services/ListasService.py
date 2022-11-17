import sys

sys.path.append('../')

from repositories.ListasRepository import ListasRepository

class ListasService:

    async def getListaById(idUsuario):

        response = await ListasRepository.getListaById(idUsuario)

        #TRATAMENTOS AQUI

        return response

    async def gravaLivroLista(item):

        response = await ListasRepository.getListaById(item)

        #TRATAMENTOS AQUI

        return response


    async def removeLivroLista(idLista):

        response = await ListasRepository.getListaById(idLista)

        #TRATAMENTOS AQUI

        return response
    