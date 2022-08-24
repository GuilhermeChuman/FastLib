class GenerosQueries:
    
    getAll = "SELECT * FROM Generos"

    getById = "SELECT * FROM Generos WHERE id = :id"

    add =  "INSERT INTO Generos(nome, descricao) " 
    add += "VALUES (:nome, :descricao)"

    edit =  "UPDATE Generos " 
    edit += "SET nome = :nome, descricao = :descricao "
    edit += "WHERE id = :id"

    delete = "DELETE FROM Generos WHERE id = :id"
