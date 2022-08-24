class LogsQueries:
    
    getAll = "SELECT Logs.*, TipoLog.descricao FROM Logs "
    getAll += "INNER JOIN TipoLog ON(Logs.idTipoLog = TipoLog.id)"
