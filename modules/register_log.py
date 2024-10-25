from datetime import datetime


def registrar_log(conn, arquivo, responsavel, status, mensagem):
    cursor = conn.cursor()
    query = "INSERT INTO transacao_log (arquivo, responsavel, data_hora, status, mensagem) VALUES (%s, %s, %s, %s, %s)"
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    valores = (arquivo, responsavel, data_hora, status, mensagem)
    cursor.execute(query, valores)
    conn.commit()