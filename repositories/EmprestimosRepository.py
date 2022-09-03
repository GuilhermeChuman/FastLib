import sys

sys.path.append('../')

from env import DB
from queries.EmprestimosQueries import EmprestimosQueries

class EmprestimosRepository:

    async def getEmprestimos():

        query = EmprestimosQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        
        return rows
