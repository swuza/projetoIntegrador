import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("MYSQL_PUBLIC_URL")
engine = create_engine(DATABASE_URL)

def carregar_dados(query):
    dados_df = pd.read_sql(query, engine)
    return dados_df