import sys

sys.path.append('../')

from services.GenerosService import GenerosService

class GenerosController:

    async def getGeneros():

        try:

            response = await GenerosService.getGeneros()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def getGeneroById(id):

        try:

            response = await GenerosService.getGeneroById(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def addGenero(item):

        try:

            response = await GenerosService.addGenero(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def editGenero(id, item):

        try:

            response = await GenerosService.editGenero(id, item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def deleteGenero(id):

        try:

            response = await GenerosService.deleteGenero(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}