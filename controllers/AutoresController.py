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

    async def addAutor(item):

        try:

            await DB.connection.connect()
            query = AutoresQueries.add
            values = [
                item
            ]
            await DB.connection.execute_many(query=query, values=values)
            data = await DB.last_inserted_id('Autores')
            await DB.connection.disconnect()

            return { "success": True, "message":"OK", "data": data}
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}

    async def getAutorById(id):

        try:

            values = {'id': id}
            await DB.connection.connect()
            query = AutoresQueries.getById
            rows = await DB.connection.fetch_one(query=query, values=values)
            await DB.connection.disconnect()
            print(rows)
            if rows == None:
                return {"success":True, "message":"Data not found", "data":None}
            else:
                return {"success":True, "message":"OK", "data":rows}
                    
        except Exception as e:

            return { "success": False, "message":"error", "data": None}    

    async def editAutor(id, item):

        try:

            currentData = await AutoresController.getAutorById(id)
            if(currentData['data'] == None):
                return { "success": False, "message":"Gênero não encontrado", "data": None}   

            item['id'] = id
            await DB.connection.connect()
            query = AutoresQueries.edit
            values = [
                item
            ]
            await DB.connection.execute_many(query=query, values=values)
            await DB.connection.disconnect()

            return { "success": True, "message":"OK", "data": item}
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}    

    async def deleteAutor(id):

        try:

            currentData = await AutoresController.getAutorById(id)
            if(currentData['data'] == None):
                return { "success": False, "message":"Autor não encontrado", "data": None}   

            values = {'id': id}
            await DB.connection.connect()
            query = AutoresQueries.delete
            await DB.connection.execute(query=query, values=values)
            await DB.connection.disconnect()

            return { "success": True, "message":"OK", "data": None}
        
        except Exception as e:

            return { "success": False, "message":"Erro Interno", "data": None}    