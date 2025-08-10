import random
import string

def gerar_senha(comprimento):
    """
    Gera uma senha aleatória com o comprimento especificado.

    A senha incluirá uma combinação de letras maiúsculas e minúsculas,
    dígitos e caracteres especiais.
    """
    if comprimento < 4:
        print("O comprimento da senha deve ser de pelo menos 4 caracteres para garantir a inclusão de todos os tipos de caracteres.")
        return None

    # Define os caracteres que serão utilizados na senha
    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = string.punctuation

    # Garante que a senha contenha pelo menos um de cada tipo de caractere
    senha_temporaria = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]

    # Combina todos os caracteres para o restante da senha
    todos_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais

    # Preenche o restante da senha com caracteres aleatórios
    for _ in range(comprimento - 4):
        senha_temporaria.append(random.choice(todos_caracteres))

    # Embaralha a senha para garantir a aleatoriedade da posição dos caracteres
    random.shuffle(senha_temporaria)

    # Converte a lista de caracteres em uma string
    return "".join(senha_temporaria)

if __name__ == "__main__":
    try:
        comprimento_senha = int(input("Digite a quantidade de caracteres para a nova senha: "))
        senha_gerada = gerar_senha(comprimento_senha)
        if senha_gerada:
            print(f"Sua senha aleatória é: {senha_gerada}")
    except ValueError:
        print("Por favor, digite um número inteiro válido para o comprimento da senha.")