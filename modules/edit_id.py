def editar_registro(conn, id_registro, nome, valor):
    cursor = conn.cursor()
    query = "UPDATE funcionarios SET nome = %s, empresa = %s WHERE id_funcionario = %s"
    cursor.execute(query, (nome, valor, id_registro))
    query = "UPDATE uso_convenio SET nome = %s, empresa = %s WHERE id_funcionario = %s"
    cursor.execute(query, (nome, valor, id_registro))
    conn.commit()