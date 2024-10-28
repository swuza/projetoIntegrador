import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.getenv("MYSQL_PUBLIC_URL")

engine = create_engine(DATABASE_URL)

try:
    connection = engine.connect()
    print("conexao realizada com sucesso")
    connection.close()
except Exception as e:
    print(f'erro ao conectar: {e}')