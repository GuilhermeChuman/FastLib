class UsuariosQueries:
    
    getAll = "SELECT id, nome FROM Usuarios"

    getById = "SELECT * FROM Usuarios WHERE id = :id"

    add =  "INSERT INTO Usuarios(login, password, nome, email, validationToken, status) " 
    add += "VALUES (:login, :password, :nome, :email, :validationToken, :status)"

    edit =  "UPDATE Usuarios " 
    edit += "SET login = :login, password = :password, nome = :nome, email = :email, "
    edit += "validationToken = :validationToken, status = :status " 
    edit += "WHERE id = :id"

    delete = "DELETE FROM Usuarios WHERE id = :id"

    auth = "SELECT * FROM Usuarios WHERE login = :login AND password = :password"

