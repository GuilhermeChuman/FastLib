class EditorasQueries:
    
    getAll = "SELECT * FROM editoras"

    getById = "SELECT * FROM editoras WHERE id = :id"

    add =  "INSERT INTO editoras(nome) " 
    add += "VALUES (:nome)"

    edit =  "UPDATE editoras " 
    edit += "SET nome = :nome "
    edit += "WHERE id = :id"

    delete = "DELETE FROM editoras WHERE id = :id"
