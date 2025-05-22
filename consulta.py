import csv
import requests
import time

def consultar_cnpjs(caminho_csv):
    resultados = []
    with open(caminho_csv, newline='') as csvfile:
        cnpjs = [linha[0].strip() for linha in csv.reader(csvfile)]
    for cnpj in cnpjs:
        print(f"Consultando CNPJ: {cnpj}...")
        if not cnpj.isdigit() or len(cnpj) != 14:
            print(f"CNPJ inválido: {cnpj}")
            continue
        url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                dados = resposta.json()
                resultados.append(dados)
                print(f"Consulta OK: {cnpj}")
            else:
                print(f"Erro na consulta do CNPJ {cnpj}: {resposta.status_code}")
        except Exception as e:
            print(f"Erro ao consultar {cnpj}: {e}")
        time.sleep(1)
    return resultados