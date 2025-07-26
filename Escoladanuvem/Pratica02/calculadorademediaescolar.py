# 1. Definição das notas do aluno
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# 2. Cálculo da média
# Soma as três notas e divide o resultado por 3
media = (nota1 + nota2 + nota3) / 3

# 3. Exibição dos resultados
print("--- Boletim do Aluno ---")
print("Notas obtidas:")
# Formata as notas para exibição com duas casas decimais, para consistência
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print("------------------------")
# Formata a média final com duas casas decimais, conforme solicitado
print(f"Média Final: {media:.2f}")