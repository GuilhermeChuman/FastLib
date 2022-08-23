import sys

sys.path.append('../')

from env import database
from queries import GenerosQueries

class GenerosController:

    async def getGeneros():
        await database.connect()
        query = GenerosQueries.getAll
        rows = await database.fetch_all(query=query)
        await database.disconnect()
        return rows
