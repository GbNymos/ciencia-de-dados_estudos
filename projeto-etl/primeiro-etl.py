#extraindo dados(ids) do arquivo csv.  
# url=  https://sdw-2023-prd.up.railway.app/users/
# 


sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

import pandas as pd
df=pd.read_csv("planilha-ids.csv") #ler a planilha.
user_ids=df["UserID"].tolist() # criar uma lista com os ids da planilha(numeros que estao abaixo so titulo "UserID")
#print(user_ids)


import requests
import json
def get_user(id):
    resposta=requests.get(f"{sdw2023_api_url}/users/{id}")
    return resposta.json() if resposta.status_code == 200 else None##  possui uma condicao de que se o status code fot igual a 200 significa que e sucesso e ele retorna um arquivo json.

users=[user for id in user_ids if (user := get_user(id)) is not None] #3comprenssao de listas, possui um for e condicoes . ele filtra os que nao retorna none.
print(json.dumps(users,indent=2)) ## mostra o arquivo formatado, user e a variavel de cima


""" 
### openai_api_key ='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'
import openai
#inicializando a openai
openai.api_key = openai_api_key

#integrando com o chat gpt e criando um chat="vc e um especialista bancario".
def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
    model="gpt-2",
    messages=[
      {
          "role": "system",
          "content": "Você é um especialista em markting bancário."
      },
      {
          "role": "user",
          "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 80 caracteres)"
      }
    ]
  )
  return completion.choices[0].message.content.strip('\"') ## acessar as respostas

for user in users:                 ## percorrer os usuarios e mandar as mensagens personalizadas
  news = generate_ai_news(user)
  print(news) ### 

### era pra ser dessa forma, mas devido a : "openai.error.RateLimitError: You exceeded your current quota, please check your plan and billing details."
por isso irei eu mesma , concluir esse exercicio de forma simples.
"""
# função para criar mensagens personalizadas sem a api
def generate_custom_news(user):
    return f"Olá {user['name']}, aqui está uma mensagem sobre a importância dos investimentos: Investir pode ajudar a garantir seu futuro financeiro."


# Gere e imprima as mensagens personalizadas para cada usuário
for user in users:
    news = generate_custom_news(user)
    print(news)
# adicionando as mensagens para a lista de news do usuario
user['news'].append({
    "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
    "description": news
  })

## atualizando a api com as mensagens
def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False

for user in users:
  success = update_user(user)
  print(f"User {user['name']} updated? {success}!")