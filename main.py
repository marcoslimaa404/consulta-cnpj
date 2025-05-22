from consulta import consultar_cnpjs
from planilha import gerar_planilha
from email_sender import enviar_email_com_anexo

def main():
    print("Iniciando consulta de CNPJs...")
    cnpjs_consultados = consultar_cnpjs("cnpjs.csv")
    print("Consulta finalizada. Gerando planilha...")
    caminho_planilha = gerar_planilha(cnpjs_consultados)
    print("Planilha gerada. Enviando por e-mail...")
    enviar_email_com_anexo(caminho_planilha)
    print("Processo concluído.")

if __name__ == "__main__":
    main()