# Importando as bibliotecas necessárias
import requests
import os
from dotenv import load_dotenv

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtendo a chave da API que foi salva como variável de ambiente
API_KEY = os.getenv('API_KEY')

# URL base da API
url = 'https://api.openweathermap.org/data/2.5/weather'

# Configurando os parâmetros de consulta
params = {
    'q': 'Goiânia',
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'pt_br'
}

# Fazendo a requisição GET com parâmetros de consulta
response = requests.get(url, params=params)
data = response.json()

# Retornando a resposta
print(data)