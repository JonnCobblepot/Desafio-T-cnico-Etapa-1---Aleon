DESAFIO TÉCNICO ETAPA 1 - ALEON / IPSENSE

Projeto: Análise dps Personagens da API Marvel

Objetivo do projeto:
Este projeto tem como objetivo extrair informações de personagens da Marvel através da API pública dela, realizando algumas análises sobre os dados obtidos através da URL de requisição calculada após seu calculo. Além disso, a respeito dos dados extraídos, é gerado gráficos pelo Matplotlib que permitem uma melhor visualização dos dados pelo usuário e assim uma possível análise do que se vê.

Dependências:
- hashlib
- time
- requests
- pandas
- matplotlib

Como rodar o código:
1. Instale as bibliotecas necessárias através do comando:
   pip install -r requirements.txt
2. Execute o arquivo `main.py` para rodar o programa. 
3. Você pode verificar o passo a passo do desenvolvimento deste desafio no notebook `storytelling.ipynb`.

Funções:
- generate_parameter(): Gera a URL de requisição da API Marvel. Essa função utiliza as chaves pública e privada, o timestamp, o hash e a quantidade de personagens desejada. Retorna a URL formatada para a requisição

- extraction_data(): Extrai os dados da API Marvel a partir da requisição URL da função anterior, extraindo em formato JSON. Retorna a lista de personagens se a requisição for um sucesso, ou None se falhar

- plot_gBarra_contagem_por_ano(df): Plota um gráfico de barras com a contagem de personagens modificados por ano

- plot_gPercentual_descricao(df): Plota um gráfico de pizza com o percentual de personagens com e sem descrição

- plot_gDispersao_id_ano(df): Plota um gráfico de dispersão que relaciona os ID dos personagens com anos de modificação

- main(): Executa o programa principal chamando todas as funções

Objetivos atendidos do projeto:
- Foi extraido dados da API Marvel escolhida
- Os dados da API foram formatados de forma tabular utilizando a biblioteca Pandas
- Foi criado gráficos utilizando o Matplotlib para análise dos dados
- O DataFrame foi transformado visando para que os dados sejam usados convenientemente
- Foi utilizado o versionamento com o Git
- Há muitos comentários no código além da docstring
- Foi colocado análise de erros e seu tratamento nas condicionais do código
- Há um arquivo storytelling para verificação do passo a passo do planejamento e desenvolvimento deste desafio

Contato: +55 16 99993-0311
Nome: João Pedro Fernandes
E-mail: joao.cobblepot7@gmail.com
