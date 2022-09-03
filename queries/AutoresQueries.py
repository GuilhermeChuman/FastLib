class AutoresQueries:
    
    getAll = "SELECT * FROM Autores ORDER BY Autores.nome"

    getById = "SELECT * FROM Autores WHERE id = :id"

    add =  "INSERT INTO Autores(nome) " 
    add += "VALUES (:nome)"

    getAutoresByLivro = " SELECT trabalhos.id, autores.nome as 'autor' from autores "
    getAutoresByLivro += "INNER JOIN trabalhos ON(autores.id = trabalhos.idAutor) "
    getAutoresByLivro += "WHERE trabalhos.idLivro = :id"

    edit =  "UPDATE Autores " 
    edit += "SET nome = :nome "
    edit += "WHERE id = :id"

    delete = "DELETE FROM Autores WHERE id = :id"
