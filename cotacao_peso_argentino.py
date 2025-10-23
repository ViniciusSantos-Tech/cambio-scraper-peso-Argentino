#Feito por Vinicius Santos-Tech
# Web Scraper simples para cotação do Peso Argentino


from bs4 import BeautifulSoup
import requests

url = 'https://www.infomoney.com.br/ferramentas/cambio/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
linhas = soup.find_all('tr')
primeira_linha = linhas[1]
celulas = primeira_linha.find_all('td')
print("💵 COTAÇÃO PESO ARGENTINO")
print("---------------------------")
print(f"Moeda: {celulas[0].text.strip()}")
print(f"Compra: R$ {celulas[2].text.strip()}")
print(f"Venda: R$ {celulas[3].text.strip()}")
print(f"Variação: {celulas[4].text.strip()}%")
