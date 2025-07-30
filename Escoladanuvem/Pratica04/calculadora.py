def calculadora():
    print("🔢 Calculadora Simples: +  -  *  /")
    
    while True:
        try:
            # Solicita o primeiro número
            num1 = input("Digite o primeiro número: ").strip()
            num1 = float(num1)

            # Solicita o segundo número
            num2 = input("Digite o segundo número: ").strip()
            num2 = float(num2)

            # Solicita a operação
            operacao = input("Digite a operação (+, -, *, /): ").strip()

            if operacao not in ['+', '-', '*', '/']:
                raise ValueError("Operação inválida.")

            # Verifica e executa a operação
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Não é possível dividir por zero.")
                resultado = num1 / num2

            print(f"\n✅ Resultado: {num1} {operacao} {num2} = {resultado}")
            break  # Encerra o loop após operação bem-sucedida

        except ValueError as ve:
            print(f"⚠️ Erro de valor: {ve}")
        except ZeroDivisionError as zde:
            print(f"⚠️ Erro de operação: {zde}")
        except Exception as e:
            print(f"⚠️ Algo deu errado: {e}")

# Executa a calculadora
calculadora()
