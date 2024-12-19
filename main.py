import hashlib
import time
import requests


#? Função para manipular os parâmetros e retornar a URL de Requisição
def generate_parameter():

    #! Chaves publicas e privadas (coloquei as minhas para obter meus parâmetros e testar o endpoint)
    PUBLIC_KEY = "...coloque aqui sua chave pública..."
    PRIVATE_KEY = "...coloque aqui sua chave privada..."

    # Valor do ts (timestamp) sendo a data e horário atual
    ts = str(time.time())

    # Soma para concatenar no hash
    soma_hash = ts + PRIVATE_KEY + PUBLIC_KEY

    # Gerando o hash pelo md5 visto na documentação da Marvel
    hash = hashlib.md5(soma_hash.encode()).hexdigest()

    #! Indica quantos personagens/dados serão requisitados
    n_characters = str(10)

    # Formatação e formação da URL de Requisição
    URL = f'http://gateway.marvel.com/v1/public/characters?limit={n_characters}&ts={ts}&apikey={PUBLIC_KEY}&hash={hash}'

    # Retorna a URL de Requisição da API Marvel
    return URL


#? Função para extrair os dados da API da Marvel
def extraction_data():

    # Obtendo a URL
    URL = generate_parameter()

    # Fzendo a requisição
    response = requests.get(URL)

    # Verificando se a requisição foi um sucesso ou não
    if response.status_code == 200:

        # Dados retornados pela API
        data = response.json() 
        print("A Requisição URL foi um sucesso!")

        # Retorna os dados e seus resultados, extraídos do formato JSON da API
        return data['data']['results']
    
    else:
        print(f"A Requisição URL falhou. Erro na requisição: {response.status_code}")
        print(response.text)

        return None


# Dados da Marvel (nesse caso, referente aos personagens/characters, mas poderia ser comics ou outro trocando na URL)
marvel_data = extraction_data()


# Verificando se os dados foram obtidos com sucesso
if marvel_data is not None and len(marvel_data) > 0:
    print("Dados extraídos com sucesso!")
    print("-----------------------------------PERSONAGENS MARVEL-----------------------------------")

    for character in marvel_data:
        print(f"Nome: {character['name']} \nDescrição: {character['description']}")
        print("----------------------------------------------------------------------------------------")

else:
    print("Falha ao extrair os dados!")