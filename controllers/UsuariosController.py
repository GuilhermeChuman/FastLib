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
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}

    async def getUsuarioById(id):

        try:

            values = {'id': id}
            await DB.connection.connect()
            query = UsuariosQueries.getById
            rows = await DB.connection.fetch_one(query=query, values=values)
            await DB.connection.disconnect()

            if len(rows) == 0:
                return {"success":True, "message":"Data not found", "data":None}
            else:
                return {"success":True, "message":"OK", "data":rows}
                    
        except Exception as e:

            return { "success": False, "message":"error", "data": None}    

    async def editUsuario(id, item):

        try:

            currentData = await UsuariosController.getUsuarioById(id)
            if(currentData['data'] == None):
                return { "success": False, "message":"Usuário não encontrado", "data": None}   

            item['id'] = id
            await DB.connection.connect()
            query = UsuariosQueries.edit
            values = [
                item
            ]
            await DB.connection.execute_many(query=query, values=values)
            await DB.connection.disconnect()

            return { "success": True, "message":"OK", "data": item}
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}    

    async def deleteUsuario(id):

        try:

            currentData = await UsuariosController.getUsuarioById(id)
            if(currentData['data'] == None):
                return { "success": False, "message":"Usuário não encontrado", "data": None}   

            values = {'id': id}
            await DB.connection.connect()
            query = UsuariosQueries.delete
            await DB.connection.execute(query=query, values=values)
            await DB.connection.disconnect()

            return { "success": True, "message":"OK", "data": None}
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}    
        
