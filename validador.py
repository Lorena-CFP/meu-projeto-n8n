import re

def validar_email(email):
    # Checa se o formato do e-mail é válido
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(padrao, email):
        return True
    return False

# Exemplo de teste
email_teste = "teste232@n8n.com"
if validar_email(email_teste):
    print(f"O e-mail '{email_teste}' é válido!")
else:
    print(f"O e-mail '{email_teste}' é inválido.")