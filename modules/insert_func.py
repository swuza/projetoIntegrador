

def inserir_dados_func(conn, df):
    cursor = conn.cursor()
    for index, row in df.iterrows():
        query = "INSERT INTO funcionarios (id_funcionario, nome, cpf, data_nascimento, empresa, cnpj) \
            VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, tuple(row))
    conn.commit()