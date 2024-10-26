def inserir_dados_uso(conn, df):
    cursor = conn.cursor()
    for index, row in df.iterrows():
        query = "INSERT INTO uso_convenio (id_uso, id_funcionario, nome_convenio, tipo_convenio, data_uso, tipo_atendimento) \
        VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, tuple(row))
    conn.commit()