import re
import json

def extrair_metadados(texto_peticao):
    # Dicionario para armazenar os dados extraidos
    dados = {
        "qualificacao_partes": {
            "autor": "Nao identificado",
            "reu": "Nao identificado"
        },
        "ramo_do_direito": "Civil",
        "tema_principal": "Indenizacao por danos morais",
        "principais_teses": [],
        "pedidos": []
    }
    
    # Busca simples pelas partes no texto
    linhas = texto_peticao.split('\n')
    for linha in linhas:
        if "autor" in linha.lower() or "requerente" in linha.lower():
            dados["qualificacao_partes"]["autor"] = linha.strip()
        elif "réu" in linha.lower() or "requerido" in linha.lower() or "banco" in linha.lower():
            dados["qualificacao_partes"]["reu"] = linha.strip()

    # Busca por teses e pedidos basicos
    if "cdc" in texto_peticao.lower() or "consumidor" in texto_peticao.lower():
        dados["ramo_do_direito"] = "Direito do Consumidor"
        dados["principais_teses"].append("Aplicacao do Codigo de Defesa do Consumidor")
    
    if "dano moral" in texto_peticao.lower() or "danos morais" in texto_peticao.lower():
        dados["principais_teses"].append("Reparacao por danos morais")
        
    if "justiça gratuita" in texto_peticao.lower():
        dados["pedidos"].append("Concessao de justiça gratuita")
        
    return json.dumps(dados, indent=4, ensure_ascii=False)


texto_usuario = input("Cole o texto da petição aqui e pressione Enter: ")
resultado = extrair_metadados(texto_usuario)
print(resultado)
