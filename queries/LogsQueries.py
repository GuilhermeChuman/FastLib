class LogsQueries:
    
    getAll = "SELECT logs.*, lipolog.descricao FROM Logs "
    getAll += "INNER JOIN tipolog ON(Logs.idTipoLog = tipolog.id)"

    getById = getAll+" WHERE logs.id = :id"

    add =  "INSERT INTO logs(data, idTipoLog, idUsuario) " 
    add += "VALUES (:data, :idTipoLog, :idUsuario)"
