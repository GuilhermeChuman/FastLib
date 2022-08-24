import sys

sys.path.append('../')

from env import DB
from queries.UsuariosQueries import UsuariosQueries

class UsuariosController:

    async def getUsuarios():

        try:

            await DB.connection.connect()
            query = UsuariosQueries.getAll
            rows = await DB.connection.fetch_all(query=query)
            await DB.connection.disconnect()

            if len(rows) == 0:
                response = {"success":True, "message":"Data not found", "data":None}
            else:
                response = {"success":True, "message":"OK", "data":rows}
            
            return response
        
        except:

            return { "success": False, "message":"Erro Interno", "data": None}

    async def addUsuario(item):

        try:

            await DB.connection.connect()
            query = UsuariosQueries.add
            values = [
                item
            ]
            await DB.connection.execute_many(query=query, values=values)
            data = await DB.last_inserted_id('Usuarios')
            await DB.connection.disconnect()

            return { "success": True, "message":"OK", "data": data}
        
        except:

            return { "success": False, "message":"Erro Interno", "data": None}
    
        
