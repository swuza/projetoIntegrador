from database import conectar_banco


def inserir_dados_uso(df):

    conn = conectar_banco()

    for index, row in df.iterrows():
        query = "INSERT INTO uso_convenio (id_uso, id_funcionario, nome_convenio, tipo_convenio, data_uso, tipo_atendimento) \
        VALUES (%s, %s, %s, %s, %s, %s)"
        conn._cursor_execute(query, tuple(row))
    conn.commit()