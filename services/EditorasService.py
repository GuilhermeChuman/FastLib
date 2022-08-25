import sys

sys.path.append('../')

from repositories.EditorasRepository import EditorasRepository

class EditorasService:

    async def getEditoras():

        response = await EditorasRepository.getEditoras()

        #TRATAMENTOS AQUI

        return response

    async def getEditoraById(id):

        response = await EditorasRepository.getEditoraById(id)

        #TRATAMENTOS AQUI

        return response

    async def addEditora(item):

        response = await EditorasRepository.addEditora(item)

        #TRATAMENTOS AQUI

        return response

    async def editEditora(id, item):

        response = await EditorasRepository.editEditora(id, item)

        #TRATAMENTOS AQUI

        return response

    async def deleteEditora(id):

        response = await EditorasRepository.deleteEditora(id)

        #TRATAMENTOS AQUI

        return response