class LivrosQueries:
    
    getAll = "SELECT Editoras.nome, Generos.nome, Livros.* FROM Editoras "
    getAll += "INNER JOIN Livros ON(Livros.idEditora = Editoras.id) "
    getAll += "INNER JOIN Generos ON(Livros.idGenero = Generos.id)"
