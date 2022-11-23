import sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.path.append('../')

from repositories.UsuariosRepository import UsuariosRepository
from mailLayouts.activateEmail import ActivateEmail


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

    async def signup(item):

        cadUser = await UsuariosRepository.signup(item)

        body = ActivateEmail.getBody(cadUser['nome'], '')

        try:
            UsuariosServices.sendMail()

        except Exception as e:

            return e

        return cadUser


    async def sendMail(smtp_server, port, sender_email, password, receiver_email, message, subject):

        content = MIMEMultipart("alternative")
        content["Subject"] = subject
        content["From"] = sender_email
        content["To"] = receiver_email

        body = MIMEText(message, "html")

        content.attach(body)

        # Create a secure SSL context
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, content.as_string()
            )


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