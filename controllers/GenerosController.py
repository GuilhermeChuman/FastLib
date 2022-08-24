import sys

sys.path.append('../')

from env import DB
from queries.GenerosQueries import GenerosQueries

class GenerosController:

    async def getGeneros():

        try:

            await DB.connection.connect()
            query = GenerosQueries.getAll
            rows = await DB.connection.fetch_all(query=query)
            await DB.connection.disconnect()

            if len(rows) == 0:
                response = {"success":True, "message":"Data not found", "data":None}
            else:
                response = {"success":True, "message":"OK", "data":rows}

            return response
        
        except Exception as e:

            return { "success": False, "message":e.__class__, "data": None}