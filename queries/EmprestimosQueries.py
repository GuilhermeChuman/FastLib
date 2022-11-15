class EmprestimosQueries:
    
    getAll =  "SELECT Emprestimos.id, Usuarios.nome, Livros.titulo, Livros.volume, Emprestimos.dataEmprestimo, "
    getAll += "Emprestimos.dataDevolucao, Emprestimos.estado, IF( (DATEDIFF(CURDATE(),dataEmprestimo ) <= 7 OR Emprestimos.estado <> 'E'), 'OK', 'ATR') as diasEmprestimo "
    getAll += "FROM Emprestimos "
    getAll += "INNER JOIN Livros on (Emprestimos.idLivro = Livros.id) "
    getAll += "INNER JOIN Usuarios on (Emprestimos.idUsuario = Usuarios.id) "
    getAll += "ORDER BY diasEmprestimo, Emprestimos.estado, Emprestimos.dataEmprestimo"