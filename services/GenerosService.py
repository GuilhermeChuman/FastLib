import sys

sys.path.append('../')

from repositories.GenerosRepository import GenerosRepository

class GenerosService:

    async def getGeneros():

        response = await GenerosRepository.getGeneros()

        #TRATAMENTOS AQUI

        return response

    async def getGeneroById(id):

        response = await GenerosRepository.getGeneroById(id)

        #TRATAMENTOS AQUI

        return response

    async def addGenero(item):

        response = await GenerosRepository.addGenero(item)

        #TRATAMENTOS AQUI

        return response

    async def editGenero(id, item):

        response = await GenerosRepository.editGenero(id, item)

        #TRATAMENTOS AQUI

        return response

    async def deleteGenero(id):

        response = await GenerosRepository.deleteGenero(id)

        #TRATAMENTOS AQUI

        return response