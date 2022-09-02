class LivrosQueries:
    
    getAll = "SELECT Editoras.nome as 'editora', Generos.nome as 'genero', Livros.* FROM Editoras "
    getAll += "RIGHT JOIN Livros ON(Livros.idEditora = Editoras.id) "
    getAll += "LEFT JOIN Generos ON(Livros.idGenero = Generos.id) "
    getAll += "ORDER BY titulo"

    getById = "SELECT * FROM Livros WHERE id = :id"

    getAutoresByLivro = " SELECT trabalhos.id, autores.nome as 'autor' from autores "
    getAutoresByLivro += "INNER JOIN trabalhos ON(autores.id = trabalhos.idAutor) "
    getAutoresByLivro += "WHERE trabalhos.idLivro = :id"

    add = "INSERT INTO Livros(isbn, titulo, descricao, volume, palavraChave1, "
    add += "palavraChave2, palavraChave3, ano, edicao, idEditora, idGenero) "
    add += "VALUES (:isbn, :titulo, :descricao, :volume, :palavraChave1, :palavraChave2, "
    add += ":palavraChave3, :ano, :edicao, :idEditora, :idGenero)"

    edit =  "UPDATE Livros "
    edit += "SET isbn = :isbn, titulo = :titulo, descricao = :descricao, volume = :volume, "
    edit += "palavraChave1 = :palavraChave1, palavraChave2 = :palavraChave2, palavraChave3 = :palavraChave3, "
    edit += "ano = :ano, edicao = :edicao, idEditora = :idEditora, idGenero = :idGenero "
    edit += "WHERE id = :id"

    delete = " DELETE FROM Livros WHERE id = :id"

    addTrabalho = "INSERT INTO Trabalhos(idAutor, idLivro) "
    addTrabalho += "VALUES (:idAutor, :idLivro)"

    getTrabalhoById = " SELECT * FROM Trabalhos WHERE id = :id"

    removeTrabalho = " DELETE FROM Trabalhos WHERE id = :id"

    
