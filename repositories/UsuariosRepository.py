import sys
import random
import string

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

    async def validateAccount(item):

        values = item
        queryValid = UsuariosQueries.validateAccount
        rows = await DB.connection.fetch_one(query=queryValid, values=values)

        if rows == None:
            return False

        else:
            return rows

    async def identifyToken(token):

        values = {'validationToken': token}

        query = UsuariosQueries.validateToken
        rows = await DB.connection.fetch_one(query=query, values=values)

        if rows == None:
            raise Exception("Token não identificado ou expirado")

        values['newToken'] = await UsuariosRepository.generateToken()

        queryActivate =  UsuariosQueries.activateAccount
        await DB.connection.execute(query=queryActivate, values=values)

        response = {
            'login': rows['login'],
            'password': rows['password']
        }

        return response

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

    async def signup(item):

        item['validationToken'] = await UsuariosRepository.generateToken()
        item['status'] = 'T'
        item['id'] = await UsuariosRepository.addUsuario(item)
        
        
        listaQuery = UsuariosQueries.addLista
        values = {
            'idUsuario': item['id'],
            'login': item['nome']
        }

        await DB.connection.execute(query=listaQuery, values=values)
        listData = await DB.last_inserted_id('listas')
        item['idLista'] = listData['id']

        return item

    async def generateToken():

        tokenValid = False

        while not tokenValid:

            token = ''

            for i in range(15):
                token += await UsuariosRepository.randomChar(random.randrange(2))

            tokenValid = await UsuariosRepository.validateToken(token)
        
        return token 

    async def recoverPassword(data):

        newPassword = await UsuariosRepository.generateToken()

        form = {
            'login': data['login'],
            'password': newPassword,
            'nome': data['nome'],
            'email': data['email'],
            'validationToken': data['validationToken'],
            'status': data['status']
        }

        await UsuariosRepository.editUsuario(data['id'], form)

        return newPassword 
        
    async def validateToken(token):

        query = UsuariosQueries.validateToken
        rows = await DB.connection.fetch_all(query=query, values={'validationToken': token})

        if len(rows) == 0:
            return True
        else:
            return False

    async def randomChar(mode):

        match mode:

            # select 1 lowercase
            case 0:
                return random.choice(string.ascii_lowercase)

            # select 1 uppercase
            case 1:
                return random.choice(string.ascii_uppercase)

            # select 1 digit
            case 2:
                return random.choice(string.digits)

    async def addUsuario(item):

        query = UsuariosQueries.add
        values = item

        await DB.connection.execute(query=query, values=values)
        data = await DB.last_inserted_id('usuarios')

        return data['id']

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