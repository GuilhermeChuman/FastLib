import sys
from itertools import groupby
from operator import itemgetter

sys.path.append('../')

from env import DB
from queries.EmprestimosQueries import EmprestimosQueries

class EmprestimosRepository:

    async def getEmprestimos():

        query = EmprestimosQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        
        return rows

    async def emprestimosStatus():

        query = EmprestimosQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        
        obj = {}

        allSituacoes = ['S', 'E', 'A', 'D']

        newRows = []

        # Setando empréstimos atrasados
        for item in rows:
            newObj = {}
            newObj['id'] = item['id']
            newObj['nome'] = item['nome']
            newObj['titulo'] = item['titulo']
            newObj['volume'] = item['volume']
            newObj['dataEmprestimo'] = item['dataEmprestimo']
            newObj['dataDevolucao'] = item['dataDevolucao']
            newObj['diasEmprestimo'] = item['diasEmprestimo']

            if(item['diasEmprestimo'] == 'ATR'):
                newObj['estado'] = 'A'
            else:
                newObj['estado'] = item['estado']

            newRows.append(newObj)

        # Sort rows data by estado.
        newRows = sorted(newRows, key = itemgetter('estado'))
        
        # Display data grouped by estado
        for key, value in groupby(newRows, key = itemgetter('estado')):
            obj[key]  = 0
            for k in value:
                obj[key] += 1

        for val in allSituacoes:
            count = 0
            for key in obj:
                if(val == key):
                    count = obj[key]
            
            obj[val] = count

        return obj
