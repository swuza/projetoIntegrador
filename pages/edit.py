import streamlit as st

from database import conectar_banco
from modules import editar_registro



def pagina_edicao():
    st.title("Editar Registro")
    conn = conectar_banco()
    id_editar = st.number_input("Digite o ID do registro para editar", min_value=1, step=1)
    idfunc_editar = st.text_input("Novo ID funcionario")
    nome_editar = st.text_input("Novo nome")
    cpf_editar = st.number_input("Novo CPF")
    nasc_editar = st.date_input("Nova data de nascimento", format="DD/MM/YYYY")
    empresa_editar = st.text_input("Nova empresa")
    cnpj_editar = st.number_input("Novo CNPJ")

    if st.button("Salvar Edição"):
        try:
            editar_registro(conn, id_editar, idfunc_editar, nome_editar, cpf_editar, nasc_editar, empresa_editar, cnpj_editar)
            st.success(f"Registro com ID {id_editar} editado com sucesso.")
        except Exception as e:
            st.error(f"Erro ao editar o registro: {str(e)}")