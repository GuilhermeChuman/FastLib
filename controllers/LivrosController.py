import sys

sys.path.append('../')

from env import DB
from queries.LivrosQueries import LivrosQueries

class LivrosController:

    async def getLivros():

        try:

            await DB.connection.connect()
            query = LivrosQueries.getAll
            rows = await DB.connection.fetch_all(query=query)
            await DB.connection.disconnect()

            if len(rows) == 0:
                response = {"success":True, "message":"Data not found", "data":None}
            else:
                response = {"success":True, "message":"Data not found", "data":rows}
            
            return response
        
        except:

            return { "success": False, "message":"Erro Interno", "data": None}
