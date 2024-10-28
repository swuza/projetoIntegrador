from datetime import datetime
from database import conectar_banco
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

def registrar_log(arquivo, responsavel, status):
    engine = conectar_banco()
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Define a query de inserção
        query = text("""
            INSERT INTO transacao_log (arquivo, responsavel, data_hora, status)
            VALUES (:arquivo, :responsavel, :data_hora, :status)
        """)
        
        # Define os valores como um dicionário
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        valores = {"arquivo": arquivo, "responsavel": responsavel, "data_hora": data_hora, "status": status}
        
        # Executa a query com a sessão
        session.execute(query, valores)
        session.commit()  # Confirma a transação
    
    except Exception as e:
        session.rollback()  # Reverte em caso de erro
        print(f"Erro ao registrar log: {e}")
    
    finally:
        session.close()
