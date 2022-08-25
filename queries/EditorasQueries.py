class EditorasQueries:
    
    getAll = "SELECT * FROM Editoras"

    getById = "SELECT * FROM Editoras WHERE id = :id"

    add =  "INSERT INTO Editoras(nome) " 
    add += "VALUES (:nome)"

    edit =  "UPDATE Editoras " 
    edit += "SET nome = :nome "
    edit += "WHERE id = :id"

    delete = "DELETE FROM Editoras WHERE id = :id"
