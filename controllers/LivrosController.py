import sys
from urllib import response

sys.path.append('../')

from services.LivrosService import LivrosService

class LivrosController:

    async def getLivros():

        try:

            response = await LivrosService.getLivros()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def getLivrosSemEmprestimo():

        try:

            response = await LivrosService.getLivrosSemEmprestimo()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def addTrabalho(item):

        try:

            response = await LivrosService.addTrabalho(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}

    async def solicitarEmprestimo(item):

        try:

            response = await LivrosService.solicitarEmprestimo(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}

    async def aprovarEmprestimo(id):

        try:

            response = await LivrosService.aprovarEmprestimo(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}

    async def recusarEmprestimo(id):

        try:

            response = await LivrosService.recusarEmprestimo(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}
    

    async def emprestar(item):

        try:

            response = await LivrosService.emprestar(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}

    async def devolverLivro(id):

        try:

            response = await LivrosService.devolverLivro(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}

    
    async def verifySolicitacaoLivro(idUsuario, idLivro):

        try:

            response = await LivrosService.verifySolicitacaoLivro(idUsuario, idLivro)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:

            return { "success": False, "message":str(e), "data": None}

    async def verifyEmprestimoLivro(id):

        try:

            response = await LivrosService.verifyEmprestimoLivro(id)
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
