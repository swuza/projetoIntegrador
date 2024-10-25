
import streamlit as st
import pandas as pd

from database import conectar_banco
from modules import buscar_registros



def pagina_visualizacao():
    st.title("Visualização de Dados")
    conn = conectar_banco()

    # Busca por registros
    termo_busca = st.text_input("Digite um termo para buscar (nome ou empresa):")
    if termo_busca:
        resultados1, resultados2 = buscar_registros(conn, termo_busca)
        st.write("Resultados em Funcionarios:")
        st.write(resultados1)
        st.write("Resultados em Uso de Convenio:")
        st.write(resultados2)

    # Exibir todos os dados
    st.subheader("Todos os Dados da Funcionarios:")
    query1 = "SELECT * FROM Funcionarios"
    dados_df1 = pd.read_sql(query1, conn)
    st.write(dados_df1)

    st.subheader("Todos os Dados em Uso de Convenio:")
    query2 = "SELECT * FROM Uso_Convenio"
    dados_df2 = pd.read_sql(query2, conn)
    st.write(dados_df2)