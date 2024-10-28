def buscar_registros(conn, termo):
    cursor = conn.cursor(dictionary=True)

    query1 = "SELECT * FROM funcionarios WHERE nome LIKE %s OR empresa LIKE %s"
    cursor.execute(query1, ('%' + termo + '%', '%' + termo + '%'))
    resultados1 = cursor.fetchall()

    resultados2 = []

    if resultados1:

        id_funcionario = resultados1[0]['id_funcionario']

        query2 = "SELECT * FROM uso_convenio WHERE id_funcionario = %s"
        cursor.execute(query2, (id_funcionario))
        resultados2 = cursor.fetchall()

    return resultados1, resultados2