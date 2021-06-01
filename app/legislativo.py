# Exemplo de busca e dados
# import json
# from dao.engine import session
from model.congresso.despesa import DespesaDeputado
from dao.deputado_dao import DeputadoDao, DeputadoDespesaDao
# from model.congresso.deputado import Deputado

import requests

URL_DEPUTADOS = "https://dadosabertos.camara.leg.br/api/v2/deputados"

url_deputados_filter = URL_DEPUTADOS + \
    "?dataInicio=2020-01-01&dataFim=2021-12-31&ordem=ASC&ordenarPor=nome"


def get_next_url(links):

    for link in links:
        if link['rel'] == 'next':
            return link['href']
    return None


payload_dep = {}
headers_dep = {
    #  'Cookie': 'DCK=Dck04|YIIfC|YIIfC'
}

response_deputados = requests.request(
    "GET", url_deputados_filter, headers=headers_dep, data=payload_dep)

# json.loads(response_deputados.text)
deputados = response_deputados.json()['dados']

DeputadoDao.insert_or_update(deputados)

for deputado in deputados:
    print("===========================================================")
    url_despesas_filter = URL_DEPUTADOS + \
        "/"+str(deputado['id']) + \
        "/despesas?ano=2020&itens=100&ordem=ASC&ordenarPor=ano"

    payload_desp = {}
    headers_desp = {
        #  'Cookie': 'DCK=Dck04|YIIg9|YIIfC'
    }

    despesas = []
    while url_despesas_filter is not None:
        response_despesas = requests.request(
            "GET", url_despesas_filter, headers=headers_desp, data=payload_desp)
        despesas.extend(response_deputados.json()['dados'])

        print(response_despesas.json()["dados"][0])
        url_despesas_filter = get_next_url(response_despesas.json()["links"])
        print(url_despesas_filter)
        # print(response_despesas.json()["dados"][0].keys())

    DeputadoDespesaDao.insert_or_update(
        despesas, deputado['id'])
