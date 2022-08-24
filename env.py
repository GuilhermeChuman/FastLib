from databases import Database

class DB:

    DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/biblioteca"
    # SQLALCHEMY_DATABASE_URL = "127.0.0.1:8000"
    # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

    connection = Database(DATABASE_URL)

    async def last_inserted_id(table):
        return await DB.connection.fetch_all("SELECT id FROM "+table+" ORDER BY id DESC LIMIT 1")

    # await database.connect()

    #DEPENDENCIES
    # $ pip install aiomysql
    # $ pip install databases
    # $ pip install uvicorn
    # $ pip install fastapi

    #HOW TO RUN 
    # python -m uvicorn main:app --reload 
