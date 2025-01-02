# Importando as bibliotecas necessárias
from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# Inicializando a aplicação
app = Flask(__name__)

# Carregando as variáveis de ambiente do arquivo .env
load_dotenv()

# Obtendo a chave da API que foi salva como variável de ambiente
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configurando um cliente a partir da chave da API
client = OpenAI(api_key=OPENAI_API_KEY)

# Escolhendo o modelo a ser utilizado
GPT_MODEL = "gpt-3.5-turbo"

# Configurando o endpoint para geração de conteúdo via API da OpenAI
@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.json
    try:
        response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": data.get("sys_prompt")},
                {"role": "user", "content": data.get("user_prompt")}
            ],
            max_tokens=data.get("max_tokens", 250),
            temperature=data.get("temperature", 0.5),
            seed=data.get("seed")
        )
        return jsonify({"response": response.choices[0].message.content}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rodando a aplicação
if __name__ == '__main__':
    app.run(debug=True)