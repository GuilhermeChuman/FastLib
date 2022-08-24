class AutoresQueries:
    
    getAll = "SELECT * FROM Autores"

    getById = "SELECT * FROM Autores WHERE id = :id"

    add =  "INSERT INTO Autores(nome) " 
    add += "VALUES (:nome)"

    edit =  "UPDATE Autores " 
    edit += "SET nome = :nome "
    edit += "WHERE id = :id"

    delete = "DELETE FROM Autores WHERE id = :id"
