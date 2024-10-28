from database import conectar_banco
from modules import validar_csv_func, validar_csv_uso, inserir_dados_func, inserir_dados_uso, registrar_log
import streamlit as st
import pandas as pd

def pagina_upload(nome_responsavel):
    st.title("Upload de CSV")
        
    # Upload de dois arquivos CSV
    arquivo_csv1 = st.file_uploader("Escolha o arquivo de Cadastro (.csv)", type="csv")
    arquivo_csv2 = st.file_uploader("Escolha o arquivo de Uso (.csv)", type="csv")
        
    # Botão para processar os uploads
    if st.button("Processar Arquivos"):
        conn = conectar_banco()  # Conectar ao banco antes de processar

        try:
            # Processar primeiro arquivo CSV
            if arquivo_csv1 is not None:
                # Leitura do CSV
                df1 = pd.read_csv(arquivo_csv1)

                # Validar o CSV
                valido, mensagem = validar_csv_func(df1)
                if not valido:
                    st.error(f"Erro no arquivo {arquivo_csv1.name}: {mensagem}")
                else:
                    try:
                        # Inserir os dados na tabela Funcionarios
                        inserir_dados_func(df1)

                        # Registrar o log de sucesso
                        status = "Sucesso!"
                        registrar_log(arquivo_csv1.name, nome_responsavel, status)

                        st.success(f"Arquivo {arquivo_csv1.name} processado e inserido em Funcionarios com sucesso!")
                    
                    except Exception as e:
                        # Registrar o log de erro
                        status = "Erro"
                        registrar_log(arquivo_csv1.name, nome_responsavel, status)
                        st.error(f"Erro ao processar o arquivo {arquivo_csv1.name}: {str(e)}")
            else:
                st.warning("Por favor, envie o primeiro arquivo CSV.")

            # Processar segundo arquivo CSV
            if arquivo_csv2 is not None:
                # Leitura do CSV
                df2 = pd.read_csv(arquivo_csv2)

                # Validar o CSV
                valido, mensagem = validar_csv_uso(df2)
                if not valido:
                    st.error(f"Erro no arquivo {arquivo_csv2.name}: {mensagem}")
                else:
                    try:
                        # Inserir os dados na tabela Uso de Convenio
                        inserir_dados_uso(df2)

                        # Registrar o log de sucesso
                        status = "Sucesso!"
                        registrar_log(arquivo_csv2.name, nome_responsavel, status)

                        st.success(f"Arquivo {arquivo_csv2.name} processado e inserido em Uso de Convenio com sucesso!")
                    except Exception as e:
                        # Registrar o log de erro
                        status = "Erro"
                        registrar_log(arquivo_csv2.name, nome_responsavel, status)
                        st.error(f"Erro ao processar o arquivo {arquivo_csv2.name}: {str(e)}")
            else:
                st.warning("Por favor, envie o segundo arquivo CSV.")

        finally:
            # Fechar a conexão com o banco de dados após o processamento
            conn.close()

    # Instruções para o usuário
    st.info("Por favor, envie dois arquivos CSV.")