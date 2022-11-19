import sys

sys.path.append('../')

from repositories.EmprestimosRepository import EmprestimosRepository

class EmprestimosService:

    async def getEmprestimos():

        response = await EmprestimosRepository.getEmprestimos()

        #TRATAMENTOS AQUI

        return response

    async def emprestimosStatus():

        response = await EmprestimosRepository.emprestimosStatus()

        #TRATAMENTOS AQUI

        return response