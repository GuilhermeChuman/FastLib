import sys

sys.path.append('../')

from services.EmprestimosService import EmprestimosService

class EmprestimosController:

    async def getEmprestimos():

        try:

            response = await EmprestimosService.getEmprestimos()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def EmprestimosService():

        try:

            response = await EmprestimosService.getEmprestimos()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}