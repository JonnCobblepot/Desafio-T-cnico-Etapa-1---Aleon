import hashlib
import time
import requests
import pandas as pd
import matplotlib.pyplot as plt


#? Função para manipular os parâmetros e retornar a URL de Requisição
def generate_parameter():
    """
    Gera a URL de requisição da API Marvel
    Essa função utiliza as chaves pública e privada, o timestamp, o hash e a quantidade de personagens desejada.

    Retorna a URL formatada para a requisição
    """

    #! Chaves publicas e privadas (coloquei as minhas para obter meus parâmetros e testar o endpoint)
    PUBLIC_KEY = "f957679ebe331b5cb3de7d6bc8531e39"
    PRIVATE_KEY = "07f8a233c3b078deb6371d3a7a988461c0e2bc42"

    # Valor do ts (timestamp) sendo a data e horário atual
    ts = str(time.time())

    # Soma para concatenar no hash
    soma_hash = ts + PRIVATE_KEY + PUBLIC_KEY

    # Gerando o hash pelo md5 visto na documentação da Marvel
    hash = hashlib.md5(soma_hash.encode()).hexdigest()

    #! Indica quantos personagens/dados serão requisitados
    n_characters = str(100)

    # Formatação e formação da URL de Requisição
    URL = f'http://gateway.marvel.com/v1/public/characters?limit={n_characters}&ts={ts}&apikey={PUBLIC_KEY}&hash={hash}'

    # Retorna a URL de Requisição da API Marvel
    return URL


#? Função para extrair os dados da API da Marvel
def extraction_data():
    """
    Extrai os dados da API Marvel a partir da requisição URL da função anterior, extraindo em formato JSON

    Retorna a lista de personagens se a requisição for um sucesso, ou None se falhar
    """

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


#? Função para plotar o gráfico de barras com a contagem por ano de modificação
def plot_gBarra_contagem_por_ano(df):
    """
    Plota um gráfico de barras com a contagem de personagens modificados por ano

    Argumento: df que é DataFrame contendo a coluna 'Ano de Modificação' e sendo df_marvel 

    Returns: None, entretanto, plota o gráfico
    """

    anos = df['Ano de Modificação'].value_counts().sort_index()
    plt.figure(figsize=(5, 12))
    plt.bar(anos.index, anos.values, color='blue')
    plt.title('Quantidade de Personagens por Ano de Modificação', fontsize=14)
    plt.xlabel('Ano de Modificação', fontsize=12)
    plt.ylabel('Quantidade de Personagens', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


#? Função para plotar o gráfico de pizza com percentual dos personagens que possuem ou não descrição (seu resumo/história)
def plot_gPercentual_descricao(df):
    """
    Plota um gráfico de pizza com o percentual de personagens com e sem descrição

    Argumento: df que é DataFrame contendo a coluna 'Ano de Modificação' e sendo df_marvel 

    Returns: None, entretanto, plota o gráfico
    """

    descricao_contagem = df['Possui Descrição'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(descricao_contagem, labels=descricao_contagem.index, autopct='%1.1f%%', startangle=90, colors=['blue', 'red'])
    plt.title('Percentual de Personagens com e sem Descrição', fontsize=14)
    plt.show()


#? Função para plotar o gráfico de dispersão para análise da coexistência ou não de uma relação entre ID e Ano 
def plot_gDispersao_id_ano(df):
    """
    Plota um gráfico de dispersão que relaciona os ID dos personagens com anos de modificação

    Argumento: df que é DataFrame contendo a coluna 'Ano de Modificação' e sendo df_marvel 

    Returns: None, entretanto, plota o gráfico
    """

    plt.figure(figsize=(10, 6))
    plt.scatter(df['ID'], df['Ano de Modificação'], alpha=0.7, color='green')
    plt.title('Relação entre ID e Ano de Modificação', fontsize=14)
    plt.xlabel('ID', fontsize=12)
    plt.ylabel('Ano de Modificação', fontsize=12)
    plt.grid(alpha=0.5)
    plt.tight_layout()
    plt.show()


#? Função principal para a execução do programa
def main():
    """
    Executa o programa principal chamando todas as funções

    Returns: None, mas executa e chama as demais funções para plotar gráficos e output tabular dos dados
    """

    # Dados da Marvel (nesse caso, referente aos personagens/characters, mas poderia ser comics ou outro trocando na URL)
    marvel_data = extraction_data()

    # Verificando se os dados foram obtidos com sucesso e caso sim, os mostra na saída, agora de forma tabular    
    if marvel_data is not None and len(marvel_data) > 0:
        print("Dados extraídos com sucesso!")
        print("-----------------------------------PERSONAGENS MARVEL-----------------------------------")

        # Uma list comprehension já adiantando a parte de simplificação do código, aqui a respeito da renomeação das classes dos characters
        marvel_table = [{"ID": character['id'],
                         "Nome": character['name'],
                         "Descrição": character['description'],
                         "Modificado em": character['modified']}
                        for character in marvel_data]
        
        # Passando para um DataFrame do Pandas
        df_marvel = pd.DataFrame(marvel_table)

        # Alterando a formatação de 'modified'
        df_marvel['Modificado em'] = pd.to_datetime(df_marvel['Modificado em'], errors='coerce', utc=True)

        # Conseguindo somente o ano da modificação
        df_marvel['Ano de Modificação'] = df_marvel['Modificado em'].dt.year
        
        # Verificando quais personagens possuem ou não sua descrição
        df_marvel['Possui Descrição'] = df_marvel['Descrição'].apply(lambda x: 'Sim' if pd.notna(x) and x != '' else 'Não')


        # Mostrando os dados na tela de forma tabular
        print("\nDados na formatação tabular com Pandas:")
        print(df_marvel)

        # Plotando os gráficos
        plot_gBarra_contagem_por_ano(df_marvel)
        plot_gPercentual_descricao(df_marvel)
        plot_gDispersao_id_ano(df_marvel)

    else:
        print("Falha ao extrair os dados.")


#? Execução do programa
if __name__ == "__main__":
    main()