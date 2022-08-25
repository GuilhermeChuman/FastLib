import sys

sys.path.append('../')

from env import DB
from queries.LogsQueries import LogsQueries

class LogsRepository:

    async def getLogs():

        await DB.connection.connect()
        query = LogsQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        await DB.connection.disconnect()
        
        return rows

    async def getLogById(id):

        values = {'id': id}
        await DB.connection.connect()
        query = LogsQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)
        await DB.connection.disconnect()

        if rows == None:
            raise Exception("Log não encontrado")

        else:
            return rows

    async def addLog(item):

        await DB.connection.connect()
        query = LogsQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Logs')
        await DB.connection.disconnect()

        return data