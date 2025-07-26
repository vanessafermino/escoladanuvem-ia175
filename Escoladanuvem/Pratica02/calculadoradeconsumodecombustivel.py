# 1. Definição dos dados da viagem
distancia_percorrida = 300.0  # em quilômetros (km)
combustivel_gasto = 25.0      # em litros (l)

# 2. Cálculo do consumo médio
# A fórmula é a distância total dividida pelo total de combustível gasto.
consumo_medio = distancia_percorrida / combustivel_gasto

# 3. Exibição dos resultados de forma organizada
print("--- Relatório de Consumo da Viagem ---")
print("Dados da Viagem:")
# Formata os dados de entrada e o resultado com 2 casas decimais
print(f"Distância Percorrida: {distancia_percorrida:.2f} km")
print(f"Combustível Gasto: {combustivel_gasto:.2f} litros")
print("----------------------------------------")
print("Resultado Final:")
print(f"Consumo Médio: {consumo_medio:.2f} km/l")