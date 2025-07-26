# 1. Lê o número do funcionário (inteiro).
numero_funcionario = int(input("Digite o número do funcionário: "))

# 2. Lê a quantidade de horas trabalhadas (inteiro).
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))

# 3. Lê o valor recebido por hora (ponto flutuante/decimal).
valor_por_hora = float(input("Digite o valor recebido por hora: "))

# 4. Calcula o salário multiplicando as horas pelo valor por hora.
salario = horas_trabalhadas * valor_por_hora

# 5. Imprime os resultados no formato exato solicitado.
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = R$ {salario:.2f}")