import os
import dotenv
import google.generativeai as genai

dotenv.load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 256,
    "stop_sequences": [
        "6",
    ]
}

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "você é um cactegorizador de produtos"
  },
  {
    "role": "model",
    "parts": "**Categoria:** Higiene pessoal\n\n**Subcategoria:** Cuidados bucais\n\n**Características:**\n\n* Cerdas macias ou médias\n* Cabeça pequena ou média\n* Cabo reto ou angular\n* Cabo antiderrapante\n* Cor variada\n\n**Usos:**\n\n* Limpar os dentes\n* Remover a placa e os restos de comida\n* Prevenir a cárie\n* Clarear os dentes\n* Massagear as gengivas\n* Melhorar o hálito\n\n**Benefícios:**\n\n* Previne problemas bucais\n* Melhora a saúde bucal geral\n* Aumenta a autoestima\n* É um produto acessível e fácil de encontrar"
  }
])

convo.send_message("escova de dente")
print(convo.last.text)