def classificar_idade():
  """
  Solicita a idade do usuário e a classifica em uma categoria.
  """
  try:
    # Solicita a idade e converte a entrada para um número inteiro
    idade = int(input("Digite a sua idade: "))

    # Verifica se a idade é um número não negativo
    if idade < 0:
      print("Por favor, digite um número válido para a idade.")
    # Classifica a idade nas categorias especificadas
    elif 0 <= idade <= 12:
      print("Classificação: Criança")
    elif 13 <= idade <= 17:
      print("Classificação: Adolescente")
    elif 18 <= idade <= 59:
      print("Classificação: Adulto")
    else: # Se a idade for 60 ou mais
      print("Classificação: Idoso")

  except ValueError:
    # Executado se o usuário não digitar um número inteiro
    print("Erro: Entrada inválida. Por favor, digite apenas números.")

# Chama a função para iniciar o programa
classificar_idade()