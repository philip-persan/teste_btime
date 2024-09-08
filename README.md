# Documentação - Scripts de Coleta de Dados

## Descrição Geral

Este projeto contém dois scripts que automatizam a coleta de dados de ações listadas na bolsa de valores:

1. **Script 1: Web Scraping**  
   Esse script coleta dados de ações utilizando técnicas de web scraping com a biblioteca BeautifulSoup no site Fundamentus.

2. **Script 2: API Pública**  
   Esse script utiliza a API pública da Alpha Vantage para coletar dados de cotações mensais de ações e salvar essas informações em um arquivo CSV.

---

## Dependências

Ambos os scripts requerem as seguintes bibliotecas Python:

- **Requests**: Para realizar as requisições HTTP tanto no web scraping quanto na API.
- **BeautifulSoup4**: Utilizada no Script 1 para analisar o HTML e extrair os dados.
- **CSV**: Módulo embutido no Python para salvar os dados extraídos em arquivos CSV.

### Instalação das Dependências

Você pode instalar as dependências utilizando o `pip`:

```bash
pip install requests beautifulsoup4
```

---

## Script 1: Web Scraping

### Descrição

Este script coleta dados de ações diretamente do site Fundamentus usando a biblioteca BeautifulSoup. Ele navega na tabela de resultados, extrai as informações de cada ação e as salva em um arquivo CSV.

### Instruções de Execução

1. **Certifique-se de que as dependências estão instaladas.**
2. **Execute o script no terminal ou no seu ambiente de desenvolvimento:**

```bash
python scirpt_1_web_scraping_bs4.py
```

3. **Resultado**: Um arquivo chamado `dados_fundamentus_webscarping.csv` será gerado com as informações extraídas.

### Estrutura do CSV

O arquivo CSV conterá as seguintes colunas:

```
Papel, Preço, P/L, P/VP, PSR, Div. Yield, P/Ativo, P/Cap.Giro, P/EBIT, P/ACL, EV/EBIT, EV/EBITDA, Mrg Ebit, Mrg. Líq., ROIC, ROE, Liquidez, Patrim. Líq, Dív.Brut/Patrim., Cresc. Rec. 5a
```

### Tratamento de Erros

O script inclui verificações para tratar erros comuns, como a ausência de células ou falhas no carregamento da página. Se o script não conseguir encontrar a tabela desejada, ele falhará de maneira segura e não tentará processar dados inválidos.

---

## Script 2: API Pública

### Descrição

Este script coleta dados de cotações mensais de ações usando a API pública da Alpha Vantage. Ele realiza uma requisição à API, formata os dados recebidos, e os salva em um arquivo CSV.

### Instruções de Execução

1. **Certifique-se de que as dependências estão instaladas.**
2. **Obtenha uma chave da API Alpha Vantage [aqui](https://www.alphavantage.co/support/#api-key).**
3. **Substitua a variável `API_KEY` no script pela sua chave da API.**
4. **Execute o script no terminal ou no seu ambiente de desenvolvimento:**

```bash
python script_2_api_request.py
```

5. **Resultado**: Um arquivo chamado `dados_alphavantage_api.csv` será gerado com as informações extraídas.

### Estrutura do CSV

O arquivo CSV conterá as seguintes colunas:

```
Data, Abertura, Alta, Baixa, Fechamento, Volume
```

### Tratamento de Erros

O script inclui tratamento básico de erros, como a verificação do código de status da resposta (`status_code`) e a validação dos dados JSON retornados para garantir que eles estão no formato esperado. Se algum erro ocorrer, o script exibirá uma mensagem e encerrará a execução.

---

## Estrutura de Pastas

```
.
├── scirpt_1_web_scraping_bs4.py
├── script_2_api_request.py
├── dados_fundamentus_webscarping.csv
├── dados_alphavantage_api.csv
└── README.md
```

---

## Documentação Extra

### Como Usar o GitHub para Hospedar o Projeto

Após criar os dois scripts e os arquivos CSV, você deve enviar o código para um repositório GitHub. Aqui estão os passos básicos:

1. **Inicie um repositório Git:**

```bash
git init
```

2. **Adicione os arquivos:**

```bash
git add .
```

3. **Faça o commit dos arquivos:**

```bash
git commit -m "Adicionando scripts de coleta de dados"
```

4. **Conecte-se ao GitHub e envie os arquivos:**

```bash
git remote add origin <url-do-repositorio>
git push -u origin master
```
