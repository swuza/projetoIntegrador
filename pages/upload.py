import streamlit as st
import pandas as pd

from database import conectar_banco
from modules import validar_csv, inserir_dados_func, inserir_dados_uso, registrar_log


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