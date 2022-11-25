import sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sys.path.append('../')

from repositories.UsuariosRepository import UsuariosRepository
from mailLayouts.activateEmail import ActivateEmail
from env import Mail


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

        mail = await ActivateEmail.getBody(cadUser['nome'], 'http://localhost:4200/auth/activateLogin?token=')

        cadUser['emailEnviado'] = await UsuariosServices.sendMail(cadUser['email'], mail['body'], mail['subject'])

        return cadUser

    async def identifyToken(token):

        data = await UsuariosRepository.identifyToken(token)

        return data


    async def sendMail(receiver_email, message, subject):

        mailConf = await Mail.getMailConfigs()

        content = MIMEMultipart("alternative")
        content["Subject"] = subject
        content["From"] = mailConf['sender_email']
        content["To"] = receiver_email

        body = MIMEText(message, "html")

        content.attach(body)

        # Create a secure SSL context
        try:

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(mailConf['smtp_server'], mailConf['port'], context=context) as server:
                server.login(mailConf['sender_email'], mailConf['password'])
                server.sendmail(mailConf['sender_email'], receiver_email, content.as_string())

        except Exception as e:

            return e

        return True


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