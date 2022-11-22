class AutoresQueries:
    
    getAll = "SELECT * FROM autores ORDER BY autores.nome"

    getById = "SELECT * FROM autores WHERE id = :id"

    add =  "INSERT INTO autores(nome) " 
    add += "VALUES (:nome)"

    getAutoresByLivro = " SELECT trabalhos.id, autores.nome as 'autor' from autores "
    getAutoresByLivro += "INNER JOIN trabalhos ON(autores.id = trabalhos.idAutor) "
    getAutoresByLivro += "WHERE trabalhos.idLivro = :id"

    edit =  "UPDATE autores " 
    edit += "SET nome = :nome "
    edit += "WHERE id = :id"

    delete = "DELETE FROM Autores WHERE id = :id"
