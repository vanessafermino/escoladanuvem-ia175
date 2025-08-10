import json

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, "w") as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
        print(f"Dados salvos em {nome_arquivo}.")        
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

dados = {
    "nome": "Joice",
    "idade": 29,
    "cidade": "Curitiba"
}

if __name__== "_main_":
    nome_arquivo = input("Digite o nome do arquivo JSON: ").strip()
    escrever_json(nome_arquivo, dados)
    ler_json(nome_arquivo)