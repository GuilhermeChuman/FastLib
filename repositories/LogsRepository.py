import sys

sys.path.append('../')

from env import DB
from queries.LogsQueries import LogsQueries

class LogsRepository:

    async def getLogs():

        query = LogsQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        
        return rows

    async def getLogById(id):

        values = {'id': id}
        query = LogsQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Log não encontrado")

        else:
            return rows

    async def addLog(item):

        query = LogsQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Logs')

        return data