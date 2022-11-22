from datetime import datetime

class LivrosQueries:
    
    getAll = "SELECT status.nome as status, status.cor, editoras.nome as 'editora', generos.nome as 'genero', livros.* FROM editoras "
    getAll += "RIGHT JOIN livros ON(livros.idEditora = editoras.id) "
    getAll += "LEFT JOIN generos ON(livros.idGenero = generos.id) "
    getAll += "LEFT JOIN  lista_livros "
    getAll +=     "ON( lista_livros.idLivro = livros.id ) "
    getAll += "LEFT JOIN status "
    getAll +=     "ON( status.id = lista_livros.idStatus ) "
    getAll += "ORDER BY titulo"

    totalLivros = "SELECT count(*) as total FROM livros"

    totalEmprestados =  "SELECT count(*) as total FROM livros "
    totalEmprestados += "INNER JOIN emprestimos ON(Emprestimos.idLivro = livros.id AND emprestimos.estado = 'E')"

    livrosPorGenero =  "SELECT COALESCE(generos.nome, 'NULL') as 'genero', Count(livros.titulo)  as total "
    livrosPorGenero += "FROM livros "
    livrosPorGenero += "LEFT JOIN generos ON(livros.idGenero = generos.id) "
    livrosPorGenero += "GROUP BY genero "

    emprestimosPorLivro =  "SELECT livros.id, livros.titulo, editoras.nome as 'editora', generos.nome as 'genero', count(livros.id) as total FROM editoras "
    emprestimosPorLivro += "RIGHT JOIN livros ON(Livros.idEditora = editoras.id) "
    emprestimosPorLivro += "LEFT JOIN generos ON(Livros.idGenero = generos.id) "
    emprestimosPorLivro += "INNER JOIN emprestimos ON(emprestimos.idLivro = livros.id)"
    emprestimosPorLivro += "GROUP BY livros.id"

    emprestimosPorGenero =  "SELECT generos.id, generos.nome as 'genero', count('genero') as total FROM editoras "
    emprestimosPorGenero += "RIGHT JOIN livros ON(livros.idEditora = editoras.id) "
    emprestimosPorGenero += "LEFT JOIN generos ON(livros.idGenero = generos.id) "
    emprestimosPorGenero += "INNER JOIN emprestimos ON(emprestimos.idLivro = livros.id)"
    emprestimosPorGenero += "GROUP BY generos.id"

    getAllSemEmprestimo = "SELECT editoras.nome as 'editora', generos.nome as 'genero', livros.* FROM editoras "
    getAllSemEmprestimo += "RIGHT JOIN livros ON(Livros.idEditora = editoras.id) "
    getAllSemEmprestimo += "LEFT JOIN generos ON(Livros.idGenero = generos.id) "
    getAllSemEmprestimo += "LEFT JOIN emprestimos ON(emprestimos.idLivro = livros.id AND (emprestimos.estado <> 'E' OR emprestimos.estado IS NULL)) "
    getAllSemEmprestimo += "ORDER BY titulo"

    getById = "SELECT editoras.nome as 'editora', Generos.nome as 'genero', livros.* FROM editoras "
    getById += "RIGHT JOIN livros ON(livros.idEditora = editoras.id) "
    getById += "LEFT JOIN generos ON(livros.idGenero = generos.id) "
    getById += "WHERE livros.id = :id"

    getAutoresByLivro = " SELECT trabalhos.id, autores.nome as 'autor' from autores "
    getAutoresByLivro += "INNER JOIN trabalhos ON(autores.id = trabalhos.idAutor) "
    getAutoresByLivro += "WHERE trabalhos.idLivro = :id"

    solicitarEmprestimo = " INSERT INTO emprestimos(idUsuario, idLivro, dataEmprestimo, estado) "
    solicitarEmprestimo += "VALUES (:idUsuario, :idLivro, :dataEmprestimo, 'S') "

    emprestar = " INSERT INTO emprestimos(idUsuario, idLivro, dataEmprestimo, estado) "
    emprestar += "VALUES (:idUsuario, :idLivro, :dataEmprestimo, 'E') "

    aprovarEmprestimo = " UPDATE emprestimos "
    aprovarEmprestimo += "SET estado = 'E', dataEmprestimo = '"+datetime.today().strftime('%Y-%m-%d')+"' "
    aprovarEmprestimo += "WHERE emprestimos.id = :id"

    recusarEmprestimo = " DELETE FROM emprestimos "
    recusarEmprestimo += "WHERE emprestimos.id = :id"
    
    getEmprestimoById = " SELECT * FROM emprestimos "
    getEmprestimoById += "WHERE emprestimos.id = :id"

    verifyEmprestimoLivro = " SELECT * FROM emprestimos "
    verifyEmprestimoLivro += "WHERE emprestimos.idLivro = :id AND emprestimos.estado = 'E'"

    verifySolicitacaoLivro = " SELECT * FROM emprestimos "
    verifySolicitacaoLivro += "WHERE emprestimos.idLivro = :idLivro AND emprestimos.idUsuario = :idUsuario "
    verifySolicitacaoLivro += "AND emprestimos.estado <> 'D'"

    devolverLivro = " UPDATE emprestimos "
    devolverLivro += "SET estado = 'D', dataDevolucao = :dataDevolucao "
    devolverLivro += "WHERE emprestimos.id = :idEmprestimo"

    getLivrosOnList =  "SELECT livros.*, status.nome as 'status'  FROM livros "
    getLivrosOnList += "LEFT JOIN lista_livros ON(Livros.id = lista_livros.idLivro) "
    getLivrosOnList += "INNER JOIN listas ON(lista_livros.idLista = listas.id) "
    getLivrosOnList += "INNER JOIN status ON(lista_livros.idStatus = status.id) "
    getLivrosOnList += "WHERE listas.idUsuario = :id"

    add = "INSERT INTO livros(isbn, titulo, descricao, volume, palavraChave1, "
    add += "palavraChave2, palavraChave3, ano, edicao, idEditora, idGenero) "
    add += "VALUES (:isbn, :titulo, :descricao, :volume, :palavraChave1, :palavraChave2, "
    add += ":palavraChave3, :ano, :edicao, :idEditora, :idGenero)"

    edit =  "UPDATE livros "
    edit += "SET isbn = :isbn, titulo = :titulo, descricao = :descricao, volume = :volume, "
    edit += "palavraChave1 = :palavraChave1, palavraChave2 = :palavraChave2, palavraChave3 = :palavraChave3, "
    edit += "ano = :ano, edicao = :edicao, idEditora = :idEditora, idGenero = :idGenero "
    edit += "WHERE id = :id"

    delete = " DELETE FROM livros WHERE id = :id"

    addTrabalho = "INSERT INTO trabalhos(idAutor, idLivro) "
    addTrabalho += "VALUES (:idAutor, :idLivro)"

    getTrabalhoById = " SELECT * FROM trabalhos WHERE id = :id"

    removeTrabalho = " DELETE FROM trabalhos WHERE id = :id"

    
