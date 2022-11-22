class EmprestimosQueries:
    
    getAll =  "SELECT emprestimos.id, usuarios.nome, livros.titulo, livros.volume, emprestimos.dataEmprestimo, "
    getAll += "emprestimos.dataDevolucao, emprestimos.estado, IF( (DATEDIFF(CURDATE(),dataEmprestimo ) <= 7 OR emprestimos.estado <> 'E'), 'OK', 'ATR') as diasEmprestimo "
    getAll += "FROM emprestimos "
    getAll += "INNER JOIN livros on (emprestimos.idLivro = livros.id) "
    getAll += "INNER JOIN usuarios on (emprestimos.idUsuario = usuarios.id) "
    getAll += "ORDER BY diasEmprestimo, emprestimos.estado, emprestimos.dataEmprestimo"