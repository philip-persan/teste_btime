import csv

import requests
from bs4 import BeautifulSoup

# * URL do site de onde os dados serão coletados
# * O site contém informações financeiras de empresas listadas na bolsa
url = 'https://www.fundamentus.com.br/resultado.php'

# * Header para evitar bloqueios durante o scraping
# * Simula uma requisição vinda de um navegador Firefox rodando no Windows 10
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",  # noqa
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",  # noqa
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Cache-Control": "max-age=0",
}

try:
    # * Fazendo a requisição para o site usando a URL e o header definido
    response = requests.get(url, headers=header)
    response.raise_for_status()  # * Verifica se a resposta foi bem-sucedida
except requests.exceptions.HTTPError as http_err:
    print(f"Erro HTTP ao acessar o site: {http_err}")
    exit(1)  # * Finaliza o script em caso de erro HTTP
except requests.exceptions.RequestException as err:
    print(f"Erro ao acessar o site: {err}")
    exit(1)  # * Finaliza o script em caso de erro geral

# * Parsing do conteúdo HTML retornado usando BeautifulSoup
# * Criando o objeto BeautifulSoup para manipular os dados em formato HTML
soup_data = BeautifulSoup(response.text, 'html.parser')

# * Localizando todas as linhas da tabela de dados (tr)
# * O conteúdo relevante está dentro dessas linhas
linhas_tabela = soup_data.find_all('tr')

# * Inicializando uma lista para armazenar os dados extraídos de cada linha
dados = []

# * Iterando sobre cada linha da tabela encontrada
for linha in linhas_tabela:
    # * Dentro de cada linha, procuramos as células (td)
    celulas_tabela = linha.find_all('td')

    # * Verificamos se a linha contém dados (se há células)
    if len(celulas_tabela) > 0:
        try:
            # * Extraindo e limpando o texto de cada célula
            dados_linha = [celula.text.strip() for celula in celulas_tabela]
            # * Adicionando os dados extraídos à lista
            dados.append(dados_linha)
        except Exception as e:
            # * Tratamento de erros caso haja falha na extração dos dados
            print(f"Erro ao processar a linha da tabela: {e}")

# * Tentando salvar os dados extraídos em um arquivo CSV
try:
    with open('dados_fundamentus_webscarping.csv', mode='w', newline='', encoding='utf-8') as file:  # noqa
        writer = csv.writer(file)

        # * Escrevendo o cabeçalho do CSV, referente aos nomes das colunas
        writer.writerow([
            'Papel', 'Preço', 'P/L', 'P/VP', 'PSR', 'Div. Yield',
            'P/Ativo', 'P/Cap.Giro', 'P/EBIT', 'P/ACL', 'EV/EBIT',
            'EV/EBITDA', 'Mrg Ebit', 'Mrg. Líq.', 'ROIC', 'ROE',
            'Liquidez', 'Patrim. Líq', 'Dív.Brut/Patrim.', 'Cresc. Rec.5a'
        ])

        # * Escrevendo os dados extraídos no CSV
        writer.writerows(dados)

    print("Dados salvos com sucesso em 'dados_fundamentus_webscarping.csv'")
except IOError as e:
    # * Tratamento de erro caso não seja possível criar ou salvar o arquivo
    print(f"Erro ao salvar os dados no arquivo CSV: {e}")
