from openpyxl import Workbook

def gerar_planilha(empresas):
    wb = Workbook()
    ws = wb.active
    ws.title = "Empresas"

    cabecalhos = [
        "CNPJ", "Tipo de Unidade", "Razão Social", "Nome Fantasia", "Situação Cadastral",
        "Data da Situação Cadastral", "Data de Início da Atividade", "CEP",
        "UF", "Município", "Telefone 1", "Telefone 2"
    ]
    ws.append(cabecalhos)

    for empresa in empresas:
        linha = [
            empresa.get("cnpj", ""),
            empresa.get("descricao_matriz_filial", ""),
            empresa.get("razao_social", ""),
            empresa.get("nome_fantasia", ""),
            empresa.get("descricao_situacao_cadastral", ""),
            empresa.get("data_situacao_cadastral", ""),
            empresa.get("data_inicio_atividade", ""),
            empresa.get("cep", ""),
            empresa.get("uf", ""),
            empresa.get("municipio", ""),
            empresa.get("ddd_telefone_1", ""),
            empresa.get("ddd_telefone_2", "")
        ]
        ws.append(linha)

    caminho = "resultado_consultas.xlsx"
    wb.save(caminho)
    return caminho