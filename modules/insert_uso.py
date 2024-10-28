from database import conectar_banco


def inserir_dados_uso(df):

    conn = conectar_banco()

    try:
        # Iniciando uma transação explícita
        with conn.begin():
            for _, row in df.iterrows():
                query = """
                    INSERT INTO uso_convenio (id_uso, id_funcionario, nome_convenio, tipo_convenio, data_uso, tipo_atendimento) \
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                # Passa `row` como tupla para garantir que está no formato certo
                conn.execute(query, tuple(row))
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conn.close()