import re

def eh_palindromo(frase):
  """
  Verifica se uma palavra ou frase é um palíndromo.

  Args:
    frase: A string a ser verificada.

  Returns:
    "Sim" se a frase for um palíndromo, "Não" caso contrário.
  """
  # Remove espaços, pontuação e converte para minúsculas
  frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
  
  # Inverte a string limpa
  frase_invertida = frase_limpa[::-1]
  
  # Compara a string limpa com a sua versão invertida
  if frase_limpa == frase_invertida:
    return "Sim"
  else:
    return "Não"

# --- Exemplos de uso ---
print(f"'Anotaram a data da maratona' é um palíndromo? {eh_palindromo('Anotaram a data da maratona')}")
print(f"'ovo' é um palíndromo? {eh_palindromo('ovo')}")
print(f"'Ame a ema' é um palíndromo? {eh_palindromo('Ame a ema')}")
print(f"'Gemini' é um palíndromo? {eh_palindromo('Gemini')}")
print(f"'Socorram-me, subi no ônibus em Marrocos' é um palíndromo? {eh_palindromo('Socorram-me, subi no ônibus em Marrocos')}")