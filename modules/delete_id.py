def deletar_registro(conn, id_registro):
    cursor = conn.cursor()
    query = "DELETE FROM funcionarios WHERE id_Funcionario = %s"
    cursor.execute(query, (id_registro,))
    cursor.execute("DELETE FROM uso_convenio WHERE id_Funcionario = %s", (id_registro,))
    conn.commit()