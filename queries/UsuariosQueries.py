class UsuariosQueries:
    
    getAll = "SELECT * FROM Usuarios"

    add =  "INSERT INTO Usuarios(login, password, nome, email, validationToken, status) " 
    add += "VALUES (:login, :password, :nome, :email, :validationToken, :status)"

