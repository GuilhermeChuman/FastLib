import sys

sys.path.append('../')

from services.AutoresService import AutoresService

class AutoresController:

    async def getAutores():

        try:

            response = await AutoresService.getAutores()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def autoresByLivro(id):

        try:
            
            response = await AutoresService.autoresByLivro(id)
            return { "success": True, "message":"OK", "data":response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}

    async def addAutor(item):

        try:

            response = await AutoresService.addAutor(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def addAutoresLot(item):

        try:
            
            response = await AutoresService.addAutoresLot(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def getAutorById(id):

        try:

            response = await AutoresService.getAutorById(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def editAutor(id, item):

        try:

            await AutoresController.getAutorById(id)
            response = await AutoresService.editAutor(id, item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None} 

    async def deleteAutor(id):

        try:

            await AutoresController.getAutorById(id)
            response = await AutoresService.deleteAutor(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}  