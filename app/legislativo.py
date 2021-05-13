# Exemplo de busca e dados
#import json
import requests

url_deputados = "https://dadosabertos.camara.leg.br/api/v2/deputados?dataInicio=2020-01-01&dataFim=2021-12-31&ordem=ASC&ordenarPor=nome"

payload_dep={}
headers_dep = {
#  'Cookie': 'DCK=Dck04|YIIfC|YIIfC'
}

response_deputados = requests.request("GET", url_deputados, headers=headers_dep, data=payload_dep)

deputados = response_deputados.json()#json.loads(response_deputados.text)
for deputado in deputados['dados']:
    print(deputado['nome'], deputado['id'])
#print(json_data)

print("===========================================================")
url_despesas = "https://dadosabertos.camara.leg.br/api/v2/deputados/204554/despesas?ano=2020&itens=100&ordem=ASC&ordenarPor=ano"

payload_desp={}
headers_desp = {
#  'Cookie': 'DCK=Dck04|YIIg9|YIIfC'
}

response_despesas = requests.request("GET", url_despesas, headers=headers_desp, data=payload_desp)
#print(response_despesas.text)

