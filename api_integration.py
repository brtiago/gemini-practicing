"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import os
from google.colab import userdata

os.environ['API_KEY'] = userdata.get('API_KEY')

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 5,
  "max_output_tokens": 2048,
  "stop_sequences": [
    "3:",
  ],
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
    "parts": "você é um gerador de produtos fictícios, gere cinco produtos"
  },
  {
    "role": "model",
    "parts": "1. **Óculos de Realidade Virtual com Inteligência Artificial**\n\nEsses óculos combinam a tecnologia de realidade virtual com inteligência artificial para criar uma experiência imersiva e personalizada. Eles podem se adaptar às preferências do usuário, oferecendo conteúdo relevante e experiências personalizadas.\n\n2. **Roupa Inteligente com Monitoramento de Saúde**\n\nEssas roupas incorporam sensores avançados que monitoram os sinais vitais do usuário, como frequência cardíaca, pressão arterial e temperatura corporal. Eles podem fornecer alertas em tempo real sobre problemas de saúde e enviar dados para o médico do usuário para análise.\n\n3. **Geladeira Inteligente com Reconhecimento de Alimentos**\n\nEssa geladeira usa câmeras e inteligência artificial para reconhecer os alimentos armazenados e rastrear suas datas de validade. Ela pode enviar notificações quando os alimentos estão prestes a estragar e sugerir receitas com base nos ingredientes disponíveis.\n\n4. **Carro Autônomo com Aprendizado de Máquina**\n\nEsses carros usam uma combinação de sensores, câmeras e inteligência artificial para navegar pelas ruas sem a intervenção humana. Eles podem aprender com a experiência, melhorando suas habilidades de direção com o tempo.\n\n5. **Assistente Pessoal Virtual com Personalidade Única**\n\nEsses assistentes pessoais virtuais possuem personalidades únicas e podem se adaptar às preferências do usuário. Eles podem fornecer informações, executar tarefas e até mesmo conversar com o usuário de forma natural."
  },
  {
    "role": "user",
    "parts": "você é um gerador de produtos fictícios, gere cinco produtos. e você deve gerar apenas o nome dos produtos que o usuario solicitar"
  },
  {
    "role": "model",
    "parts": "1. **Cama Inteligente com Monitoramento do Sono** - **SonoSereno**\n2. **Espelho Inteligente com Realidade Aumentada** - **Espelho Mágico**\n3. **Roupa Inteligente com Controle de Temperatura** - **ClimaVest**\n4. **Drone de Entrega Autônomo** - **EntregaExpress**\n5. **Impressora 3D de Alimentos** - **FoodPrinter**"
  },
  {
    "role": "user",
    "parts": "quero mais 4 produtos"
  },
  {
    "role": "model",
    "parts": "1. **Óculos de Realidade Aumentada para Educação** - **EduAR**\n2. **Robô de Limpeza Autônomo com Inteligência Artificial** - **Robô LimpaTudo**\n3. **Tradutor Universal em Tempo Real** - **Tradutor Global**\n4. **Dispositivo de Teletransporte Virtual** - **TeleTrans**"
  },
  {
    "role": "user",
    "parts": "<div>"
  },
  {
    "role": "user",
    "parts": "<br>"
  },
  {
    "role": "user",
    "parts": "</div>"
  },
  {
    "role": "user",
    "parts": "<div>"
  },
  {
    "role": "user",
    "parts": "<br>"
  },
  {
    "role": "user",
    "parts": "</div>"
  },
  {
    "role": "model",
    "parts": "1. **Gerador de Energia Limpa a partir do Ar** - **ArLimpoPower**\n2. **Máquina de Reciclagem Doméstica** - **ReciclaTudo**\n3. **Roupa Inteligente com Proteção Solar** - **SolarShield**\n4. **Implante Cerebral para Melhoria da Memória** - **MemóriaMax**"
  }
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)