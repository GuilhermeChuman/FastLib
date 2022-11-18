import sys

sys.path.append('../')

from services.ListasService import ListasService

class ListasController:

    async def getListaById(id):

        try:

            response = await ListasService.getListaById(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}


    async def getStatus():

        try:

            response = await ListasService.getStatus()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}


    async def gravaLivroLista(item):

        try:

            response = await ListasService.gravaLivroLista(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}


    async def removeLivroLista(idLista):

        try:

            response = await ListasService.removeLivroLista(idLista)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}
