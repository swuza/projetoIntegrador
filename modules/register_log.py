from datetime import datetime

from database import conectar_banco

def registrar_log(arquivo, responsavel, status):
    
    conn = conectar_banco()

    query = "INSERT INTO transacao_log (arquivo, responsavel, data_hora, status) VALUES (%s, %s, %s, %s)"
    data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    valores = (arquivo, responsavel, data_hora, status)

    conn._cursor_execute(query, valores)

    conn.commit()