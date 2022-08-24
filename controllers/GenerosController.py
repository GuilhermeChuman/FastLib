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

            if rows == None:
                response = {"success":True, "message":"Data not found", "data":None}
            else:
                response = {"success":True, "message":"OK", "data":rows}

            return response
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}

    async def addGenero(item):

        try:

            await DB.connection.connect()
            query = GenerosQueries.add
            values = [
                item
            ]
            await DB.connection.execute_many(query=query, values=values)
            data = await DB.last_inserted_id('Generos')
            await DB.connection.disconnect()

            return { "success": True, "message":"OK", "data": data}
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}

    async def getGeneroById(id):

        try:

            values = {'id': id}
            await DB.connection.connect()
            query = GenerosQueries.getById
            rows = await DB.connection.fetch_one(query=query, values=values)
            await DB.connection.disconnect()
            print(rows)
            if rows == None:
                return {"success":True, "message":"Data not found", "data":None}
            else:
                return {"success":True, "message":"OK", "data":rows}
                    
        except Exception as e:

            return { "success": False, "message":"error", "data": None}    

    async def editGenero(id, item):

        try:

            currentData = await GenerosController.getGeneroById(id)
            if(currentData['data'] == None):
                return { "success": False, "message":"Gênero não encontrado", "data": None}   

            item['id'] = id
            await DB.connection.connect()
            query = GenerosQueries.edit
            values = [
                item
            ]
            await DB.connection.execute_many(query=query, values=values)
            await DB.connection.disconnect()

            return { "success": True, "message":"OK", "data": item}
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}    

    async def deleteGenero(id):

        try:

            currentData = await GenerosController.getGeneroById(id)
            if(currentData['data'] == None):
                return { "success": False, "message":"Gênero não encontrado", "data": None}   

            values = {'id': id}
            await DB.connection.connect()
            query = GenerosQueries.delete
            await DB.connection.execute(query=query, values=values)
            await DB.connection.disconnect()

            return { "success": True, "message":"OK", "data": None}
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}    