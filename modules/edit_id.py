def editar_registro(conn, id_registro, nome, valor):
    cursor = conn.cursor()
    query = "UPDATE Funcionarios SET Nome = %s, Empresa = %s WHERE ID_Funcionario = %s"
    cursor.execute(query, (nome, valor, id_registro))
    query = "UPDATE Uso_Convenio SET Nome = %s, Empresa = %s WHERE ID_Funcionario = %s"
    cursor.execute(query, (nome, valor, id_registro))
    conn.commit()