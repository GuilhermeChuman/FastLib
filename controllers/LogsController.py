import sys

sys.path.append('../')

from services.LogsService import LogsService

class LogsController:

    async def getLogs():

        try:

            response = await LogsService.getLogs()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def getLogById(id):

        try:

            response = await LogsService.getLogById(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def addLog(item):

        try:

            response = await LogsService.addLog(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}
        
