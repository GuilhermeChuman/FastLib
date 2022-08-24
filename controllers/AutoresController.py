import sys

sys.path.append('../')

from env import DB
from queries.AutoresQueries import AutoresQueries

class AutoresController:

    async def getAutores():

        try:

            await DB.connection.connect()
            query = AutoresQueries.getAll
            rows = await DB.connection.fetch_all(query=query)
            await DB.connection.disconnect()

            if len(rows) == 0:
                response = {"success":True, "message":"Data not found", "data":None}
            else:
                response = {"success":True, "message":"Data not found", "data":rows}
            
            return response
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}
