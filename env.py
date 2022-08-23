from databases import Database

DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/biblioteca"
# SQLALCHEMY_DATABASE_URL = "127.0.0.1:8000"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = Database(DATABASE_URL)

# await database.connect()
