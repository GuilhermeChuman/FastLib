import sys

sys.path.append('../')

from env import CsvReader
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
        return response

    async def addGeneroLot(item):

        data = await CsvReader.readFile(item) 
        response = await GenerosRepository.addGeneroLot(data)
        return response

    async def editGenero(id, item):

        response = await GenerosRepository.editGenero(id, item)
        return response

    async def deleteGenero(id):

        response = await GenerosRepository.deleteGenero(id)

        #TRATAMENTOS AQUI

        return response