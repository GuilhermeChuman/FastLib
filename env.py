from databases import Database
import codecs
import csv
from io import BytesIO

class DB:

    DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/biblioteca"
    #DATABASE_URL = "host='127.0.0.1',user=username, passwd=password,db=database_name"
    # SQLALCHEMY_DATABASE_URL = "127.0.0.1:8000"
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

    connection = Database(DATABASE_URL)

    async def last_inserted_id(table):
        return await DB.connection.fetch_all("SELECT id FROM "+table+" ORDER BY id DESC LIMIT 1")

class CsvReader:

    async def readFile(file):

        csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
        data = []
        for rows in csvReader: 
            dct = { k: None if not v else v for k, v in rows.items() }
            data.append(dct)  

        return data

