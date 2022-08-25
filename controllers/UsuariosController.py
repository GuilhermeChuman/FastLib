import sys

sys.path.append('../')

from services.UsuariosService import UsuariosServices

class UsuariosController:

    async def getUsuarios():

        try:

            response = await UsuariosServices.getUsuarios()
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def getUsuarioById(id):

        try:

            response = await UsuariosServices.getUsuarioById(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def auth(item):

        try:

            response = await UsuariosServices.auth(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def addUsuario(item):

        try:

            response = await UsuariosServices.addUsuario(item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def editUsuario(id, item):

        try:

            response = await UsuariosServices.editUsuario(id, item)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}

    async def deleteUsuario(id):

        try:

            response = await UsuariosServices.deleteUsuario(id)
            return { "success": True, "message":"OK", "data": response}

        except Exception as e:
            
            return { "success": False, "message":str(e), "data": None}
        
