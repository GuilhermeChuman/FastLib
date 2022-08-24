import sys

sys.path.append('../')

from env import DB
from queries.EditorasQueries import EditorasQueries

class EditorasController:

    async def getEditoras():

        try:

            await DB.connection.connect()
            query = EditorasQueries.getAll
            rows = await DB.connection.fetch_all(query=query)
            await DB.connection.disconnect()

            if len(rows) == 0:
                response = {"success":True, "message":"Data not found", "data":None}
            else:
                response = {"success":True, "message":"OK", "data":rows}
            
            return response

        except:

            return { "success": False, "message":"Erro Interno", "data": None}
