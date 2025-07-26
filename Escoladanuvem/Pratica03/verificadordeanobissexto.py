def verificar_ano_bissexto():
    """
    Solicita um ano ao usuário e determina se ele é bissexto ou não.
    """
    try:
        # Solicita o ano e converte a entrada para um número inteiro.
        ano = int(input("Digite um ano para verificar: "))

        # Anos devem ser números positivos.
        if ano <= 0:
            print("Por favor, insira um ano válido (um número positivo).")
            return

        # A regra do ano bissexto em uma única condição:
        # (Divisível por 4 E não por 100) OU (Divisível por 400)
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            print(f"✅ O ano {ano} é bissexto.")
        else:
            print(f"❌ O ano {ano} não é bissexto.")

    except ValueError:
        # Mensagem de erro se o usuário não digitar um número inteiro.
        print("Erro: Entrada inválida. Por favor, digite um número de ano válido (ex: 2024).")

# Executa a função principal do programa.
if __name__ == "__main__":
    verificar_ano_bissexto()