import streamlit as st
import pandas as pd

from database import conectar_banco


def pagina_log():
    st.title("Log de Captacao")
    conn = conectar_banco()
    query = "SELECT * FROM transacao_log"
    log_df = pd.read_sql(query, conn)
    st.write(log_df)