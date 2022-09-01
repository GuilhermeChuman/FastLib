class LivrosQueries:
    
    getAll = "SELECT Editoras.nome, Generos.nome, Livros.* FROM Editoras "
    getAll += "INNER JOIN Livros ON(Livros.idEditora = Editoras.id) "
    getAll += "INNER JOIN Generos ON(Livros.idGenero = Generos.id)"

    add = "INSERT INTO Livros(isbn, titulo, descricao, volume, palavraChave1, "
    add += "palavraChave2, palavraChave3, ano, edicao, idEditora, idGenero) "
    add += "VALUES (:isbn, :titulo, :descricao, :volume, :palavraChave1, :palavraChave2, "
    add += ":palavraChave3, :ano, :edicao, :idEditora, :idGenero)"
    
