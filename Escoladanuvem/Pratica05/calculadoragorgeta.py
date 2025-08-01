def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta/100)
    return gorjeta

total_conta = float(input("Insira o valor total da conta: "))
porcentagem = float(input("Insira o valor total da gorjeta: "))

gorjeta = calcular_gorjeta(total_conta, porcentagem)

print(f"Para uma conta de R$ {total_conta:.2f}, a gorjeta de {porcentagem}% é R$ {gorjeta:.2f}")