import hashlib
import time

def generate_parameter():

    # Chaves publicas e privadas (coloquei as minhas para obter meus parâmetros e testar o endpoint)
    PUBLIC_KEY = "..."
    PRIVATE_KEY = "..."

    # Valor do ts (timestamp) sendo a data e horário atual
    ts = str(time.time())

    # Soma para concatenar no hash
    soma_hash = ts + PRIVATE_KEY + PUBLIC_KEY

    # Gerando o hash pelo md5 visto na documentação da Marvel
    hash = hashlib.md5(soma_hash.encode()).hexdigest()

    URL = f'http://gateway.marvel.com/v1/public/characters?limit=5&ts={ts}&apikey={PUBLIC_KEY}&hash={hash}'

    return URL

# Printando os valores
#print("ts:", ts)
#print("Hash:", hash)
#print("apikey:", PUBLIC_KEY)
#print("URL:", URL)