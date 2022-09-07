import sys

sys.path.append('../')

from services.LivrosService import LivrosService

class LivrosController:

    async def getLivros():

        try:

            response = await LivrosService.getLivros()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def addTrabalho(item):

        try:

            response = await LivrosService.addTrabalho(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}

    async def removeTrabalho(id):

        try:

            response = await LivrosService.removeTrabalho(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}

    async def getLivroById(id):

        try:

            response = await LivrosService.getLivroById(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}


    async def filterLivros(item, id):
        
        try:

            response = await LivrosService.filterLivros(item, id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def addLivro(item):

        try:

            response = await LivrosService.addLivro(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def addLivrosLot(item):

        try:
            
            response = await LivrosService.addLivrosLot(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def editLivro(id, item):

        try:

            response = await LivrosService.editLivro(id, item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def deleteLivro(id):

        try:

            response = await LivrosService.deleteLivro(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}
