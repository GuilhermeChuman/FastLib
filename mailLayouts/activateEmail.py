class ActivateEmail:

    async def getBody(name, buttonLink):

        return """\
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
                    <h1>Olá, """ + name + """\</h1> 

                        Parabens por se juntar ao SilverFish!<br>

                        Sua aventura em nosso acervo está prestes a começar, basta clicar no botão abaixo para validar seu email.<br> 

                        <br>
                        <center>
                            <a target="_blank" href=" """+buttonLink+"""\ "> 
                                <button style="min-width:50px; min-height:20px;">Validar Email</button>
                            </a>
                        </center>
                        
                        <br>
                        <br>
                        
                        Caso o botão não funcione você pode copiar o link abaixo diretamente: <div class="link">http://www.realpython.com</div>
                    </p>
                </body>
            </html>
        """