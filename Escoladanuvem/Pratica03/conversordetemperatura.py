def converter_temperatura():
    """
    Programa principal para converter temperaturas entre Celsius, Fahrenheit e Kelvin.
    """
    # --- 1. Obter e validar a entrada do usuário ---
    try:
        valor_str = input("Digite a temperatura (ex: 32.5): ")
        valor = float(valor_str)

        unidade_origem_str = input("Qual a unidade de origem? (C para Celsius, F para Fahrenheit, K para Kelvin): ").upper()
        unidade_destino_str = input("Para qual unidade deseja converter? (C, F, K): ").upper()

        # Validação das unidades
        unidades_validas = ['C', 'F', 'K']
        if unidade_origem_str not in unidades_validas or unidade_destino_str not in unidades_validas:
            print("Erro: Unidade inválida. Por favor, use 'C', 'F' ou 'K'.")
            return

    except ValueError:
        print(f"Erro: '{valor_str}' não é um número válido. Por favor, insira apenas o valor numérico da temperatura.")
        return

    # --- 2. Processar a conversão ---

    # Se as unidades forem iguais, não há o que converter
    if unidade_origem_str == unidade_destino_str:
        resultado = valor
    else:
        # Conversão a partir de Celsius
        if unidade_origem_str == 'C':
            if unidade_destino_str == 'F':
                # Fórmula: F = (C * 9/5) + 32
                resultado = (valor * 9/5) + 32
            else: # Para Kelvin
                # Fórmula: K = C + 273.15
                resultado = valor + 273.15

        # Conversão a partir de Fahrenheit
        elif unidade_origem_str == 'F':
            if unidade_destino_str == 'C':
                # Fórmula: C = (F - 32) * 5/9
                resultado = (valor - 32) * 5/9
            else: # Para Kelvin
                # Fórmula: K = (F - 32) * 5/9 + 273.15
                resultado = (valor - 32) * 5/9 + 273.15

        # Conversão a partir de Kelvin
        elif unidade_origem_str == 'K':
            if unidade_destino_str == 'C':
                # Fórmula: C = K - 273.15
                resultado = valor - 273.15
            else: # Para Fahrenheit
                # Fórmula: F = (K - 273.15) * 9/5 + 32
                resultado = (valor - 273.15) * 9/5 + 32

    # --- 3. Exibir o resultado formatado ---
    
    # Dicionário para obter os símbolos corretos das unidades
    simbolos = {'C': '°C', 'F': '°F', 'K': 'K'}
    
    simbolo_origem = simbolos[unidade_origem_str]
    simbolo_destino = simbolos[unidade_destino_str]

    print("\n--- Resultado ---")
    # Exibe o resultado com duas casas decimais para melhor leitura
    print(f"{valor:.2f}{simbolo_origem} é igual a {resultado:.2f}{simbolo_destino}")

# Inicia a execução do programa
if __name__ == "__main__":
    converter_temperatura()