class GenerosQueries:
    
    getAll = "SELECT * FROM generos"

    getById = "SELECT * FROM generos WHERE id = :id"

    add =  "INSERT INTO generos(nome, descricao) " 
    add += "VALUES (:nome, :descricao)"

    edit =  "UPDATE generos " 
    edit += "SET nome = :nome, descricao = :descricao "
    edit += "WHERE id = :id"

    delete = "DELETE FROM generos WHERE id = :id"
