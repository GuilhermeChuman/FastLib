from databases import Database
import codecs
import csv
from io import BytesIO
import os

class Mail:

    async def getMailConfigs():
        
        return {
            #local configs
            'sender_email': '',
            'password': '',
            'smtp_server': 'email-ssl.com.br',
            'port': 465 


            #prod configs
            # 'sender_email': os.environ['EMAIL'],
            # 'password': os.environ['MAIL_PASSWORD'],
            # 'smtp_server': 'email-ssl.com.br',
            # 'port': 465 
        }

class DB:
    
    DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/biblioteca"
    # DATABASE_URL = os.environ['DB_URL']

    connection = Database(DATABASE_URL)

    async def last_inserted_id(table):
        return await DB.connection.fetch_one("SELECT id FROM "+table+" ORDER BY id DESC LIMIT 1")

class CsvReader:

    async def readFile(file):

        csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
        data = []
        for rows in csvReader: 
            dct = { k: None if not v else v for k, v in rows.items() }
            data.append(dct)  

        return data

