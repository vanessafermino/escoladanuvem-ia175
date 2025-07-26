# Definindo o valor de PI com a precisão solicitada
pi = 3.14159265

# Lendo o valor do raio (um número de ponto flutuante)
# A função float() converte o texto de entrada para um número com casas decimais
raio = float(input("Digite o valor do raio: "))

# Calculando a área da circunferência
# O operador ** 2 eleva o valor do raio ao quadrado
area = pi * (raio ** 2)

# Exibindo o resultado formatado com 4 casas decimais
# O f-string com :.4f garante a formatação correta
print(f"A={area:.4f}")