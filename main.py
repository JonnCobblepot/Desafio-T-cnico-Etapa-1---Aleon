import hashlib
import time
import requests

# Função para manipular os parâmetros e retornar a URL de Requisição
def generate_parameter():

    # Chaves publicas e privadas (coloquei as minhas para obter meus parâmetros e testar o endpoint)
    PUBLIC_KEY = "...coloque aqui sua chave pública..."
    PRIVATE_KEY = "...coloque aqui sua chave privada..."

    # Valor do ts (timestamp) sendo a data e horário atual
    ts = str(time.time())

    # Soma para concatenar no hash
    soma_hash = ts + PRIVATE_KEY + PUBLIC_KEY

    # Gerando o hash pelo md5 visto na documentação da Marvel
    hash = hashlib.md5(soma_hash.encode()).hexdigest()

    URL = f'http://gateway.marvel.com/v1/public/characters?limit=5&ts={ts}&apikey={PUBLIC_KEY}&hash={hash}'

    return URL


# Obtendo a URL
URL = generate_parameter()

# Fzendo a requisição
response = requests.get(URL)

# Verificando se a requisição foi um sucesso ou não
if response.status_code == 200:
    data = response.json()  # Dados retornados pela API
    print("A Requisição URL foi um sucesso!")
else:
    print(f"A Requisição URL falhou. Erro na requisição: {response.status_code}")
    print(response.text)


# Printando os valores
#print("ts:", ts)
#print("Hash:", hash)
#print("apikey:", PUBLIC_KEY)
#print("URL:", URL)