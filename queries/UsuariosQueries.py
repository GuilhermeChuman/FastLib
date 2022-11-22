class UsuariosQueries:
    
    getAll = "SELECT id, nome FROM usuarios"

    getById = "SELECT * FROM usuarios WHERE id = :id"

    add =  "INSERT INTO usuarios(login, password, nome, email, validationToken, status) " 
    add += "VALUES (:login, :password, :nome, :email, :validationToken, :status)"

    edit =  "UPDATE usuarios " 
    edit += "SET login = :login, password = :password, nome = :nome, email = :email, "
    edit += "validationToken = :validationToken, status = :status " 
    edit += "WHERE id = :id"

    delete = "DELETE FROM usuarios WHERE id = :id"

    auth = "SELECT * FROM usuarios WHERE login = :login AND password = :password"

