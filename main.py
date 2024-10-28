import streamlit as st

from pages import pagina_delecao, pagina_edicao, pagina_log, pagina_upload, pagina_visualizacao
from modules import autenticar_usuario

# Função principal
def main():
    authenticator = autenticar_usuario()
    authentication_status = authenticator.login()

    
    if st.session_state["authentication_status"]:
        authenticator.logout()
        st.sidebar.title("Menu")
        page = st.sidebar.radio("Navegação", ["Upload de CSV", "Visualização de Dados", "Deletar Registro", "Editar Registro", "Log de Transações"])
        
        if page == "Upload de CSV":
            nome_responsavel = st.session_state["name"]
            pagina_upload(nome_responsavel)
        elif page == "Visualização de Dados":
            pagina_visualizacao()
        elif page == "Deletar Registro":
            pagina_delecao()
        elif page == "Editar Registro":
            pagina_edicao()
        elif page == "Log de Transações":
            pagina_log()
    elif st.session_state[authentication_status] is False:
        st.error("Usuário/senha incorretos")

if __name__ == "__main__":
    main()
