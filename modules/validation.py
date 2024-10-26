import re


def validar_csv(df):
    # Verifica se as colunas corretas estão presentes
    if not {'nome', 'empresa'}.issubset(df.columns):
        return False, "O CSV precisa conter as colunas 'Nome' e 'Empresa'."
    
    # Verificar se a coluna 'nome' contém valores válidos (não vazios e sem caracteres especiais)
    if not df['nome'].apply(lambda x: isinstance(x, str) and re.match(r"^[A-Za-z0-9\s]+$", x)).all():
        return False, "A coluna 'nome' deve conter apenas letras, números e espaços."
    
    return True, ""