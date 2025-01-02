# Importando as bibliotecas necessárias
import requests

# Realizando a requisição para a API da AwesomeAPI para obter as últimas cotações
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()  # Converte a resposta em JSON

# Processando as cotações recebidas
dolar = str(round(float(cotacoes['USDBRL']['bid']), 2)).replace('.', ',')
euro = str(round(float(cotacoes['EURBRL']['bid']), 2)).replace('.', ',')
bitcoin = cotacoes['BTCBRL']['bid']

# Exibindo as cotações formatadas
print(f"Cotações\nDólar = R$ {dolar}\nEuro = R$ {euro}\nBitcoin = R$ {bitcoin},00")