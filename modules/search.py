def buscar_registros(conn, termo):
    cursor = conn.cursor(dictionary=True)
    query1 = "SELECT * FROM funcionarios WHERE nome LIKE %s OR empresa LIKE %s"
    cursor.execute(query1, ('%' + termo + '%', '%' + termo + '%'))
    resultados1 = cursor.fetchall()

    if resultados1:
        id_funcionario = resultados1
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM uso_convenio WHERE id_funcionario = ?", (id_funcionario))
        resultados2 = cursor.fetchall()

    return resultados1, resultados2