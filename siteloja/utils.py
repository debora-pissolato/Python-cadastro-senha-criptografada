import bcrypt 

def criptografia(senha):

    salt = bcrypt.gensalt()

    criptosenha = bcrypt.hashpw(senha.encode('utf8'),salt)
    return criptosenha.decode('utf-8')