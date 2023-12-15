"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai
import dotenv
import os

dotenv.load_dotenv()
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 256,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": "gere uma lista com 5 produtos ficticios"
  },
  {
    "role": "model",
    "parts": "1. **Drink da Felicidade:** Uma bebida refrescante que instantaneamente faz você se sentir feliz e otimista. É feito com uma mistura de frutas tropicais e ingredientes naturais que melhoram o humor.\n\n\n2. **Comida de Memória:** Uma refeição deliciosa que permite que você reviva suas memórias favoritas. É feito com ingredientes que despertam os sentidos e trazem à tona lembranças vivas e emocionantes.\n\n\n3. **Robô de Amizade:** Um robô inteligente e empático que se torna seu melhor amigo. Ele pode conversar, contar piadas, jogar jogos e oferecer suporte emocional.\n\n\n4. **Traje de Invisibilidade:** Uma roupa especial que o torna invisível para os outros. É feito com materiais avançados que dobram a luz ao seu redor, tornando-o praticamente indetectável.\n\n\n5. **Máquina do Tempo:** Um dispositivo incrível que permite que você viaje no tempo. É feito com tecnologia de ponta que permite que você visite o passado ou o futuro, explorando diferentes épocas e eventos."
  }
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)