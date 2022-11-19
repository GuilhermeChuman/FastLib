import sys

sys.path.append('../')

from env import DB
from queries.UsuariosQueries import UsuariosQueries
from queries.ListasQueries import ListasQueries

class UsuariosRepository:

    async def getUsuarios():

        query = UsuariosQueries.getAll
        rows = await DB.connection.fetch_all(query=query)
        
        return rows

    async def getUsuarioById(id):

        values = {'id': id}
        query = UsuariosQueries.getById
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Usuário não encontrado")

        else:
            return rows

    async def auth(item):

        query = UsuariosQueries.auth
        rows = await DB.connection.fetch_one(query=query, values=item)

        query = ListasQueries.getById
        lista = await DB.connection.fetch_one(query=query, values={'idUsuario':rows['id']})

        obj = {}
        obj['id']               = rows['id']
        obj['login']            = rows['login']
        obj['password']         = rows['password']
        obj['nome']             = rows['nome']
        obj['email']            = rows['email']
        obj['validationToken']  = rows['validationToken']
        obj['status']           = rows['status']
        obj['idLista']          = lista['id']

        if rows == None:
            raise Exception("Usuário ou Senha inválidos")

        else:
            return obj

    async def addUsuario(item):

        query = UsuariosQueries.add
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)
        data = await DB.last_inserted_id('Usuarios')

        return data

    async def editUsuario(id, item):

        await UsuariosRepository.getUsuarioById(id)

        item['id'] = id
        query = UsuariosQueries.edit
        values = [
            item
        ]
        await DB.connection.execute_many(query=query, values=values)

        return item

    async def deleteUsuario(id):

        await UsuariosRepository.getUsuarioById(id)

        values = {'id': id}
        query = UsuariosQueries.delete
        await DB.connection.execute(query=query, values=values)

        return True