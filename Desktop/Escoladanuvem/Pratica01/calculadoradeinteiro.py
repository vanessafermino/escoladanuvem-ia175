try:
    # Lê quatro números inteiros da entrada
    A = int(input("Digite o valor de A: "))
    B = int(input("Digite o valor de B: "))
    C = int(input("Digite o valor de C: "))
    D = int(input("Digite o valor de D: "))

    # Calcula a diferença
    DIFERENCA = (A * B) - (C * D)

    # Exibe o resultado
    print(f"DIFERENCA = {DIFERENCA}")

except ValueError:
    print("Erro: todos os valores devem ser números inteiros válidos.")
