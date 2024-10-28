from database import conectar_banco


def inserir_dados_func(df):

    conn = conectar_banco()

    for index, row in df.iterrows():
        query = "INSERT INTO funcionarios (id_funcionario, nome, cpf, data_nascimento, empresa, cnpj) \
            VALUES (%s, %s, %s, %s, %s, %s)"
        conn.execute(query, tuple(row))
    conn.commit()