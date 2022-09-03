import sys

sys.path.append('../')

from repositories.EmprestimosRepository import EmprestimosRepository

class EmprestimosService:

    async def getEmprestimos():

        response = await EmprestimosRepository.getEmprestimos()

        #TRATAMENTOS AQUI

        return response