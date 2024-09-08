import csv

import requests

# * Chave da API
API_KEY = 'I3TESXS42IG3FANU'

# * Ticker da empresa que deseja consultar
TICKER = 'PETR4.SA'

# * fsting para concatenar o TICKER e API_KEY
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={TICKER}&apikey={API_KEY}'  # noqa

# * Fazendo a requisição
response = requests.get(url)

# * Tratamento básico de erro na requisição
if response.status_code != 200:
    print(f"Erro na requisição: {response.status_code}")
    exit()

# * Pegando os dados no formato json
dados = response.json()

# * Verificando se a chave 'Monthly Time Series' existe nos dados recebidos
if "Monthly Time Series" not in dados:
    print("Dados não disponíveis.")
    exit()

# * Extraindo as séries temporais mensais
series_temporais = dados["Monthly Time Series"]

# * Salvando os dados em um arquivo CSV
with open('dados_alphavantage.csv', mode='w', newline='', encoding='utf-8') as file:  # noqa
    writer = csv.writer(file)

    # * Cabeçalho do CSV
    writer.writerow([
        'Data', 'Abertura', 'Alta', 'Baixa', 'Fechamento', 'Volume'
    ])

    # * Iterando sobre os dados e escrevendo no CSV
    for data, valores in series_temporais.items():
        writer.writerow([
            data,
            valores['1. open'],
            valores['2. high'],
            valores['3. low'],
            valores['4. close'],
            valores['5. volume']
        ])

print("Dados extraídos e salvos em 'dados_alphavantage.csv'")
