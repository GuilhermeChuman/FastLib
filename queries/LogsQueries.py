class LogsQueries:
    
    getAll = "SELECT Logs.*, TipoLog.descricao FROM Logs "
    getAll += "INNER JOIN TipoLog ON(Logs.idTipoLog = TipoLog.id)"

    getById = getAll+" WHERE Logs.id = :id"

    add =  "INSERT INTO Logs(data, idTipoLog, idUsuario) " 
    add += "VALUES (:data, :idTipoLog, :idUsuario)"
