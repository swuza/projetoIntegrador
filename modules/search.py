def buscar_registros(conn, termo):
    cursor = conn.cursor(dictionary=True)
    query1 = "SELECT * FROM Funcionarios WHERE Nome LIKE %s OR Empresa LIKE %s"
    cursor.execute(query1, ('%' + termo + '%', '%' + termo + '%'))
    resultados1 = cursor.fetchall()

    if resultados1:
        ID_Funcionario = resultados1
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Uso_Convenio WHERE ID_Funcionario = ?" (ID_Funcionario))
        resultados2 = cursor.fetchall()

    return resultados1, resultados2