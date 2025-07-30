# Contexto provável do código que gerou o erro

while True:
    entrada = input("Digite uma nota ou 'fim' para terminar: ")

    if entrada.lower() == 'fim':
        break

    try:
        # O programa tenta converter a entrada para um número
        nota = float(entrada)
        # ... (código para processar a nota) ...

    except ValueError:
        # Se a conversão falhar (ex: usuário digita "abc"),
        # este bloco é executado, mostrando a mensagem de erro.
        print("Erro: Entrada inválida. Por favor, digite um número ou 'fim'.")