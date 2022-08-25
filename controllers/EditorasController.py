import sys

sys.path.append('../')

from services.EditorasService import EditorasService

class EditorasController:

    async def getEditoras():

        try:

            response = await EditorasService.getEditoras()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def getEditoraById(id):

        try:

            response = await EditorasService.getEditoraById(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def addEditora(item):

        try:

            response = await EditorasService.addEditora(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def editEditora(id, item):

        try:

            response = await EditorasService.editEditora(id, item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def deleteEditora(id):

        try:

            response = await EditorasService.deleteEditora(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}
