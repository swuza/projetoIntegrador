

def inserir_dados_func(conn, df):
    cursor = conn.cursor()
    for index, row in df.iterrows():
        query = "INSERT INTO Funcionarios (ID_Funcionario, Nome, CPF, Data_Nascimento, Empresa, CNPJ) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, tuple(row))
    conn.commit()