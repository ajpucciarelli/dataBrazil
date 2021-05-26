# Exemplo de busca e dados
# import json
# from dao.engine import session
from dao.deputado_dao import DeputadoDao
# from model.congresso.deputado import Deputado

import requests

URL_DEPUTADOS = "https://dadosabertos.camara.leg.br/api/v2/deputados"

url_deputados_filter = URL_DEPUTADOS + \
    "?dataInicio=2020-01-01&dataFim=2021-12-31&ordem=ASC&ordenarPor=nome"

payload_dep = {}
headers_dep = {
    #  'Cookie': 'DCK=Dck04|YIIfC|YIIfC'
}

# response_deputados = requests.request(
#     "GET", url_deputados_filter, headers=headers_dep, data=payload_dep)

# deputados = response_deputados.json()  # json.loads(response_deputados.text)

# DeputadoDao.insert_or_update(deputados)

print("===========================================================")
url_despesas_filter = URL_DEPUTADOS + \
    "/204554/despesas?ano=2020&itens=100&ordem=ASC&ordenarPor=ano"

payload_desp = {}
headers_desp = {
    #  'Cookie': 'DCK=Dck04|YIIg9|YIIfC'
}

response_despesas = requests.request(
    "GET", url_despesas_filter, headers=headers_desp, data=payload_desp)
print(response_despesas.json()["dados"][0])
