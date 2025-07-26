def calcular_imc():
    """
    Solicita peso e altura do usuário, calcula o IMC e fornece a classificação.
    """
    try:
        # Solicita o peso e converte para float (número com casas decimais)
        peso = float(input("Digite seu peso em kg (ex: 70.5): "))

        # Solicita a altura e converte para float
        altura = float(input("Digite sua altura em metros (ex: 1.75): "))

        # Verifica se os valores inseridos são válidos
        if peso <= 0 or altura <= 0:
            print("Erro: O peso e a altura devem ser valores positivos.")
            return # Encerra a função se os valores forem inválidos

        # Calcula o IMC usando a fórmula: peso / (altura * altura)
        imc = peso / (altura ** 2)

        # Classifica o resultado do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else: # Para qualquer valor de IMC igual ou superior a 30
            classificacao = "Obeso"

        # Exibe o resultado formatado para o usuário
        print("\n--- Resultado ---")
        print(f"Seu IMC é: {imc:.2f}") # Formata o IMC para exibir 2 casas decimais
        print(f"Classificação: {classificacao}")

    except ValueError:
        # Mensagem exibida se o usuário digitar algo que não seja um número
        print("Erro: Entrada inválida. Por favor, digite apenas números para peso e altura.")
    except ZeroDivisionError:
        # Mensagem para o caso raro de a altura ser 0
        print("Erro: A altura não pode ser zero.")

# Chama a função para iniciar o programa
calcular_imc()