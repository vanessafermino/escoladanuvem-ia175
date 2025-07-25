reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

dolares = reais / taxa_dolar
euros = reais / taxa_euro

print(f"O valor em dólares é: ${dolares:.2f}")
print(f"O valor em euros é: €{euros:.2f}")