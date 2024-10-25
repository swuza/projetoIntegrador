def deletar_registro(conn, id_registro):
    cursor = conn.cursor()
    query = "DELETE FROM Funcionarios WHERE ID_Funcionario = %s"
    cursor.execute(query, (id_registro,))
    cursor.execute("DELETE FROM Uso_Convenio WHERE ID_Funcionario = %s", (id_registro,))
    conn.commit()