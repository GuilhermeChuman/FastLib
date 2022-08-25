import sys

sys.path.append('../')

from repositories.UsuariosRepository import UsuariosRepository

class UsuariosServices:

    async def getUsuarios():

        response = await UsuariosRepository.getUsuarios()

        #TRATAMENTOS AQUI

        return response

    async def getUsuarioById(id):

        response = await UsuariosRepository.getUsuarioById(id)

        #TRATAMENTOS AQUI

        return 
        
    async def auth(item):

        response = await UsuariosRepository.auth(item)

        #TRATAMENTOS AQUI

        return response

    async def addUsuario(item):

        response = await UsuariosRepository.addUsuario(item)

        #TRATAMENTOS AQUI

        return response

    async def editUsuario(id, item):

        response = await UsuariosRepository.editUsuario(id, item)

        #TRATAMENTOS AQUI

        return response

    async def deleteUsuario(id):

        response = await UsuariosRepository.deleteUsuario(id)

        #TRATAMENTOS AQUI

        return response