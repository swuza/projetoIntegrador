import streamlit as st
import mysql.connector
import pandas as pd
from datetime import datetime
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import re

# Função para conectar ao banco de dados
def conectar_banco():
    conn = mysql.connector.connect(
        host="localhost", 
        user="root",
        password="",
        database="captacao"
    )
    return conn

# Função para validar CSV
def validar_csv(df):
    # Verifica se as colunas corretas estão presentes
    if not {'Nome', 'Empresa'}.issubset(df.columns):
        return False, "O CSV precisa conter as colunas 'Nome' e 'Empresa'."
    
    # Verificar se a coluna 'nome' contém valores válidos (não vazios e sem caracteres especiais)
    if not df['nome'].apply(lambda x: isinstance(x, str) and re.match(r"^[A-Za-z0-9\s]+$", x)).all():
        return False, "A coluna 'nome' deve conter apenas letras, números e espaços."
    
    return True, ""

# Função para registrar log de transação
def registrar_log(conn, arquivo, responsavel, status, mensagem):
    cursor = conn.cursor()
    query = "INSERT INTO transacao_log (arquivo, responsavel, data_hora, status, mensagem) VALUES (%s, %s, %s, %s, %s)"
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    valores = (arquivo, responsavel, data_hora, status, mensagem)
    cursor.execute(query, valores)
    conn.commit()

# Função para inserir dados no banco de dados para Funcionario
def inserir_dados_func(conn, df):
    cursor = conn.cursor()
    for index, row in df.iterrows():
        query = "INSERT INTO Funcionarios (ID_Funcionario, Nome, CPF, Data_Nascimento, Empresa, CNPJ) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, tuple(row))
    conn.commit()

# Função para inserir dados no banco de dados para UsoConvenio
def inserir_dados_uso(conn, df):
    cursor = conn.cursor()
    for index, row in df.iterrows():
        query = "INSERT INTO Uso_Convenio (ID_Uso, ID_Funcionario, Nome_Convenio, Tipo_Convenio, Data_Uso, Tipo_Atendimento) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, tuple(row))
    conn.commit()

# Função para deletar um registro por ID
def deletar_registro(conn, id_registro):
    cursor = conn.cursor()
    query = "DELETE FROM Funcionarios WHERE ID_Funcionario = %s"
    cursor.execute(query, (id_registro,))
    cursor.execute("DELETE FROM Uso_Convenio WHERE ID_Funcionario = %s", (id_registro,))
    conn.commit()

# Função para editar um registro por ID
def editar_registro(conn, id_registro, nome, valor):
    cursor = conn.cursor()
    query = "UPDATE Funcionarios SET Nome = %s, Empresa = %s WHERE ID_Funcionario = %s"
    cursor.execute(query, (nome, valor, id_registro))
    query = "UPDATE Uso_Convenio SET Nome = %s, Empresa = %s WHERE ID_Funcionario = %s"
    cursor.execute(query, (nome, valor, id_registro))
    conn.commit()

# Função para buscar registros por nome ou valor
def buscar_registros(conn, termo):
    cursor = conn.cursor(dictionary=True)
    query1 = "SELECT * FROM Funcionarios WHERE Nome LIKE %s OR Empresa LIKE %s"
    cursor.execute(query1, ('%' + termo + '%', '%' + termo + '%'))
    resultados1 = cursor.fetchall()

    if resultados1:
        ID_Funcionario = resultados1
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Uso_Convenio WHERE ID_Funcionario = ?" (ID_Funcionario))
        resultados2 = cursor.fetchall()

    return resultados1, resultados2

# Configurar autenticação de usuários
def autenticar_usuario():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
        
        authenticator = stauth.Authenticate (
            config['credentials'],
            config['cookie']['name'],
            config['cookie']['key'],
            config['cookie']['expiry_days'],
        )

        return authenticator

# Página de upload de CSV
def pagina_upload(nome_responsavel):
    st.title("Upload de CSV")
    
    # Upload de dois arquivos CSV
    arquivo_csv1 = st.file_uploader("Escolha o arquivo de Cadastro (.csv)", type="csv")
    arquivo_csv2 = st.file_uploader("Escolha o arquivo de Uso (.csv)", type="csv")
    
    # Botão para processar os uploads
    if st.button("Processar Arquivos"):
        conn = conectar_banco()  # Conectar ao banco antes de processar

        # Processar primeiro arquivo CSV
        if arquivo_csv1 is not None:
            # Leitura do CSV
            df1 = pd.read_csv(arquivo_csv1)

            # Validar o CSV
            valido, mensagem = validar_csv(df1)
            if not valido:
                st.error(f"Erro no arquivo {arquivo_csv1.name}: {mensagem}")
            else:
                try:
                    # Inserir os dados na Funcionario
                    inserir_dados_func(conn, df1)

                    # Registrar o log de sucesso
                    registrar_log(conn, arquivo_csv1.name, nome_responsavel, 'Sucesso', 'Dados inseridos com sucesso na Funcionarios')

                    st.success(f"Arquivo {arquivo_csv1.name} processado e inserido na Funcionarios com sucesso!")
                except Exception as e:
                    # Registrar o log de erro
                    registrar_log(conn, arquivo_csv1.name, nome_responsavel, 'Erro', str(e))
                    st.error(f"Erro ao processar o arquivo {arquivo_csv1.name}: {str(e)}")
        else:
            st.warning("Por favor, envie o primeiro arquivo CSV.")

        # Processar segundo arquivo CSV
        if arquivo_csv2 is not None:
            # Leitura do CSV
            df2 = pd.read_csv(arquivo_csv2)

            # Validar o CSV
            valido, mensagem = validar_csv(df2)
            if not valido:
                st.error(f"Erro no arquivo {arquivo_csv2.name}: {mensagem}")
            else:
                try:
                    # Inserir os dados na UsoConvenio
                    inserir_dados_uso(conn, df2)

                    # Registrar o log de sucesso
                    registrar_log(conn, arquivo_csv2.name, nome_responsavel, 'Sucesso', 'Dados inseridos com sucesso em UsoConvenio')

                    st.success(f"Arquivo {arquivo_csv2.name} processado e inserido em UsoConvenio com sucesso!")
                except Exception as e:
                    # Registrar o log de erro
                    registrar_log(conn, arquivo_csv2.name, nome_responsavel, 'Erro', str(e))
                    st.error(f"Erro ao processar o arquivo {arquivo_csv2.name}: {str(e)}")
        else:
            st.warning("Por favor, envie o segundo arquivo CSV.")

    # Instruções para o usuário
    st.info("Por favor, envie dois arquivos CSV.")

# Página de visualização de dados
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

# Página de deleção de registros
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

# Página de edição de registros
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

# Página de log de transações
def pagina_log():
    st.title("Log de Captacao")
    conn = conectar_banco()
    query = "SELECT * FROM transacao_log"
    log_df = pd.read_sql(query, conn)
    st.write(log_df)

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
    elif st.session_state["authentication_status"] is False:
        st.error("Usuário/senha incorretos")
    elif st.session_state["authentication_status"] is None:
        st.warning("Por favor, entre com seus dados")

if __name__ == "__main__":
    main()
