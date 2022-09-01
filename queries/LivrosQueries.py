class LivrosQueries:
    
    getAll = "SELECT Editoras.nome as 'editora', Generos.nome as 'genero', Livros.* FROM Editoras "
    getAll += "RIGHT JOIN Livros ON(Livros.idEditora = Editoras.id) "
    getAll += "LEFT JOIN Generos ON(Livros.idGenero = Generos.id) "
    getAll += "ORDER BY titulo"

    add = "INSERT INTO Livros(isbn, titulo, descricao, volume, palavraChave1, "
    add += "palavraChave2, palavraChave3, ano, edicao, idEditora, idGenero) "
    add += "VALUES (:isbn, :titulo, :descricao, :volume, :palavraChave1, :palavraChave2, "
    add += ":palavraChave3, :ano, :edicao, :idEditora, :idGenero)"
    
