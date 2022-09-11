from datetime import datetime

class LivrosQueries:
    
    getAll = "SELECT Editoras.nome as 'editora', Generos.nome as 'genero', Livros.* FROM Editoras "
    getAll += "RIGHT JOIN Livros ON(Livros.idEditora = Editoras.id) "
    getAll += "LEFT JOIN Generos ON(Livros.idGenero = Generos.id) "
    getAll += "ORDER BY titulo"

    getById = "SELECT Editoras.nome as 'editora', Generos.nome as 'genero', Livros.* FROM Editoras "
    getById += "RIGHT JOIN Livros ON(Livros.idEditora = Editoras.id) "
    getById += "LEFT JOIN Generos ON(Livros.idGenero = Generos.id) "
    getById += "WHERE Livros.id = :id"

    getAutoresByLivro = " SELECT trabalhos.id, autores.nome as 'autor' from autores "
    getAutoresByLivro += "INNER JOIN trabalhos ON(autores.id = trabalhos.idAutor) "
    getAutoresByLivro += "WHERE trabalhos.idLivro = :id"

    solicitarEmprestimo = " INSERT INTO emprestimos(idUsuario, idLivro, dataEmprestimo, situacao) "
    solicitarEmprestimo += "VALUES (:idUsuario, :idLivro, :dataEmprestimo, 'S') "

    emprestar = " INSERT INTO emprestimos(idUsuario, idLivro, dataEmprestimo, situacao) "
    emprestar += "VALUES (:idUsuario, :idLivro, :dataEmprestimo, 'E') "

    aprovarEmprestimo = " UPDATE Emprestimos "
    aprovarEmprestimo += "SET situacao = 'E', dataEmprestimo = '"+datetime.today().strftime('%Y-%m-%d')+"' "
    aprovarEmprestimo += "WHERE Emprestimos.id = :id"

    getEmprestimoById = " SELECT * FROM Emprestimos "
    getEmprestimoById += "WHERE Emprestimos.id = :id"

    verifyEmprestimoLivro = " SELECT * FROM Emprestimos "
    verifyEmprestimoLivro += "WHERE Emprestimos.idLivro = :id AND Emprestimos.situacao = 'E'"

    devolverLivro = " UPDATE Emprestimos "
    devolverLivro += "SET situacao = 'D' "
    devolverLivro += "WHERE Emprestimos.id = :id"

    getLivrosOnList =  "SELECT Livros.*, Status.nome as 'status'  FROM Livros "
    getLivrosOnList += "LEFT JOIN Lista_Livros ON(Livros.id = Lista_Livros.idLivro) "
    getLivrosOnList += "INNER JOIN Listas ON(Lista_Livros.idLista = Listas.id) "
    getLivrosOnList += "INNER JOIN Status ON(Lista_Livros.idStatus = Status.id) "
    getLivrosOnList += "WHERE Listas.idUsuario = :id"

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

    
