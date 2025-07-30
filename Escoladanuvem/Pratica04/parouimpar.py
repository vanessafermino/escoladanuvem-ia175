def classificar_numeros():
    pares = 0
    impares = 0

    print("Digite números inteiros. Digite 'fim' para encerrar.")

    while True:
        entrada = input("Número: ").strip().lower()

        if entrada == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print("✅ É um número **par**.")
                pares += 1
            else:
                print("✅ É um número **ímpar**.")
                impares += 1
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número inteiro ou 'fim'.")

    print("\n📊 Resultado final:")
    print(f"Números pares: {pares}")
    print(f"Números ímpares: {impares}")

# Executa o programa
classificar_numeros()
