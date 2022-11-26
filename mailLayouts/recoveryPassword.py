class RecoveryPassword:

    async def getBody(name, password):

        return {
            'subject': 'Recuperação de Email',
            'body': """\
                <html>
                    <head>
                        <style>

                        body{
                            margin-left: 20px;
                            font-family: Roboto, "Helvetica Neue", sans-serif; 
                        }

                        h1{
                            color: #7ba0e6;
                        }

                        .link{
                            color: #7ba0e6;
                            font-weight: bold;
                        }

                        button {
                            border-radius: 3px;
                            background-color: #7ba0e6;
                            border: none;
                            color: white;
                            padding: 15px 32px;
                            text-align: center;
                            text-decoration: none;
                            display: inline-block;
                            font-size: 16px;
                            cursor: pointer;
                        }
                        
                        </style>
                    </head>
                    <body>
                        <h1>Olá, """ + name + " "+ """\
                            </h1> 

                            Aqui está sua nova senha!<br>

                            Lembre-se de não compartilhar sua senha com ninguém.<br> 

                            <br>
                            <center>
                                <h1> """+password+" "+ """\
                                </h1> 
                            </center>
                            
                            <br>
                        </p>
                    </body>
                </html>
            """
        }