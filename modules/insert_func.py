from database import conectar_banco


def inserir_dados_func(df):

    conn = conectar_banco()

    try:
        # Iniciando uma transação explícita
        with conn.begin():
            for _, row in df.iterrows():
                query = """
                    INSERT INTO funcionarios (id_funcionario, nome, cpf, data_nascimento, empresa, cnpj)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                # Passa `row` como tupla para garantir que está no formato certo
                conn.execute(query, tuple(row))
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conn.close()