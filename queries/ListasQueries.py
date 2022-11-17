class ListasQueries:
    
    verifyLivroNaLista =  "SELECT * "
    verifyLivroNaLista += "FROM lista_livros "
    verifyLivroNaLista += "INNER JOIN listas "
    verifyLivroNaLista +=   "ON( lista_livros.idLista = listas.id ) "
    verifyLivroNaLista += "WHERE lista_livros.idLivro = :idLivro "
    verifyLivroNaLista += "AND listas.idLista = :idLista "


    insertLivroLista =  "INSERT INTO lista_livros(idLista, idLivro, idStatus) "
    insertLivroLista += "VALUES (:idLista, :idLivro, :idStatus) "


    updateLivroLista =  "UPDATE lista_livros "
    updateLivroLista += "SET idLivro = :idLivro, idStatus = :idStatus "
    updateLivroLista += "WHERE idLista = :idLista"


    removeLivroLista =  "DELETE FROM lista_livros"
    removeLivroLista =+ "WHERE idLista = :idLista"


    getListaById_NumLivros =  " SELECT listas.id as idLista, listas.idUsuario, listas.login, "
    getListaById_NumLivros +=       " count(lista_livros.idLivro) as total_livros "
    getListaById_NumLivros += " FROM listas "
    getListaById_NumLivros += " LEFT JOIN lista_livros "
    getListaById_NumLivros += "     ON( lista_livros.idLista = listas.id) "
    getListaById_NumLivros += " WHERE listas.idUsuario = :idUsuario "
    getListaById_NumLivros += " GROUP BY idLista, listas.idUsuario, listas.login"
    

    getListaById =  "SELECT  livros.titulo, editoras.nome as editora, generos.nome as genero, "
    getListaById += "status.nome as status "
    getListaById += "FROM lista_livros "
    getListaById += "INNER JOIN  livros "
    getListaById +=     "ON( lista_livros.idLivro = livros.id )  "
    getListaById += "LEFT JOIN editoras "
    getListaById +=     "ON( editoras.id = livros.idEditora ) "
    getListaById += "LEFT JOIN generos "
    getListaById +=     "ON( generos.id = livros.idGenero ) "
    getListaById += "INNER JOIN status "
    getListaById +=     "ON( lista_livros.idStatus = status.id ) "
    getListaById += "WHERE lista_livros.idLista = :idLista "
    getListaById += "ORDER BY titulo"