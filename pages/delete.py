import streamlit as st

from database import conectar_banco
from modules import deletar_registro



def pagina_delecao():
    st.title("Deletar Registro")
    conn = conectar_banco()
    id_deletar = st.number_input("Digite o ID do registro para deletar", min_value=1, step=1)
    if st.button("Deletar"):
      try:
        deletar_registro(conn, id_deletar)
        st.success(f"Registro com ID {id_deletar} deletado com sucesso.")
      except Exception as e:
        st.error(f"Erro ao deletar o registro: {str(e)}")