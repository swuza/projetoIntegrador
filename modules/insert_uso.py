def inserir_dados_uso(conn, df):
    cursor = conn.cursor()
    for index, row in df.iterrows():
        query = "INSERT INTO Uso_Convenio (ID_Uso, ID_Funcionario, Nome_Convenio, Tipo_Convenio, Data_Uso, Tipo_Atendimento) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, tuple(row))
    conn.commit()