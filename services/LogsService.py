import sys

sys.path.append('../')

from repositories.LogsRepository import LogsRepository

class LogsService:

    async def getLogs():

        response = await LogsRepository.getLogs()

        #TRATAMENTOS AQUI

        return response

    async def getLogById(id):

        response = await LogsRepository.getLogById(id)

        #TRATAMENTOS AQUI

        return response

    async def addLog(item):

        response = await LogsRepository.addLog(item)

        #TRATAMENTOS AQUI

        return response