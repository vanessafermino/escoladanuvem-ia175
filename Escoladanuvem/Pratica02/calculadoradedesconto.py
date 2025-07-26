# 1. Definição dos dados do produto
nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

# 2. Cálculos
# Calcula o valor do desconto (ex: 50.00 * 0.20)
valor_desconto = preco_original * (percentual_desconto / 100)

# Calcula o preço final subtraindo o desconto do preço original
preco_final = preco_original - valor_desconto

# 3. Exibição dos resultados
print("--- Detalhes da Compra com Desconto ---")
print(f"Produto: {nome_produto}")
print("---------------------------------------")
# Formata os valores monetários com 2 casas decimais para melhor visualização
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto Aplicado: {percentual_desconto}%")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print("---------------------------------------")
print(f"Preço Final a Pagar: R$ {preco_final:.2f}")