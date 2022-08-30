import sys

sys.path.append('../')

from env import CsvReader
from repositories.AutoresRepository import AutoresRepository

class AutoresService:

    async def getAutores():

        response = await AutoresRepository.getAutores()

        #TRATAMENTOS AQUI

        return response

    async def getAutorById(id):

        response = await AutoresRepository.getAutorById(id)

        #TRATAMENTOS AQUI

        return response

    async def addAutor(item):

        response = await AutoresRepository.addAutor(item)

        #TRATAMENTOS AQUI

        return response

    async def addAutoresLot(item):

        data = await CsvReader.readFile(item) 
        response = await AutoresRepository.addAutoresLot(data)
        return response

    async def editAutor(id, item):

        response = await AutoresRepository.editAutor(id, item)

        #TRATAMENTOS AQUI

        return response

    async def deleteAutor(id):

        response = await AutoresRepository.deleteAutor(id)

        #TRATAMENTOS AQUI

        return response