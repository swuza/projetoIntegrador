from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import pymysql

load_dotenv()

DATABASE_URL = os.getenv("mysql+pymysql://root:rZfgEyBBGafsSzBCLFRJvXIUBIqoHpOw@autorack.proxy.rlwy.net:41618/railway")


# Configurar o engine de conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Configurar a sessão para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão
def conectar_banco():
    conn = SessionLocal()
    try:
        return conn
    finally:
        conn.close()