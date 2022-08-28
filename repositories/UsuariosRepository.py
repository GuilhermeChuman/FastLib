import sys

sys.path.append('../')

from env import DB
from queries.UsuariosQueries import UsuariosQueries

class UsuariosRepository:

    async def getUsuarios():

        await DB.connection.connect()
        query = UsuariosQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        await DB.connection.disconnect()
        
        return rows

    async def getUsuarioById(id):

        values = {'id': id}
        await DB.connection.connect()
        query = UsuariosQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)
        await DB.connection.disconnect()

        if rows == None:
            raise Exception("Usuário não encontrado")

        else:
            return rows

    async def auth(item):

        await DB.connection.connect()
        query = UsuariosQueries.auth
        rows = await DB.connection.fetch_one(query=query, values=item)
        await DB.connection.disconnect()

        if rows == None:
            raise Exception("Usuário ou Senha inválidos")

        else:
            return rows

    async def addUsuario(item):

        await DB.connection.connect()
        query = UsuariosQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Usuarios')
        await DB.connection.disconnect()

        return data

    async def editUsuario(id, item):

        await UsuariosRepository.getUsuarioById(id)

        item['id'] = id
        await DB.connection.connect()
        query = UsuariosQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        await DB.connection.disconnect()

        return item

    async def deleteUsuario(id):

        await UsuariosRepository.getUsuarioById(id)

        values = {'id': id}
        await DB.connection.connect()
        query = UsuariosQueries.delete
        await DB.connection.execute(query=query, values=values)
        await DB.connection.disconnect()

        return None