import datetime
def calcular_idade_nascimento(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365
    return idade_dias

ano_nasc = int (input("Digite o ano do seu nascimento:"))

idade_em_dias = calcular_idade_nascimento (ano_nasc)
print(f"Sua idade aproximada em dias é : {idade_em_dias} dias.")