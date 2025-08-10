

def consultar_cep(cep):
    """
    Consulta um CEP na API ViaCEP e retorna as informações de endereço.
    """
    # Formata a URL da API com o CEP fornecido, removendo hifens ou pontos.
    cep_formatado = cep.replace("-", "").replace(".", "")
    url = f"https://viacep.com.br/ws/{cep_formatado}/json/"

    try:
        # Realiza a requisição GET para a API
        resposta = requests.get(url)

        # Levanta um erro para respostas com status de erro (ex: 404, 500)
        resposta.raise_for_status()

        # Converte a resposta JSON em um dicionário Python
        dados = resposta.json()

        # Verifica se o CEP consultado é inválido (a API retorna um erro específico)
        if 'erro' in dados and dados['erro']:
            print(f"Erro: O CEP '{cep}' não foi encontrado ou é inválido.")
            return

        # Extrai e exibe as informações do endereço
        print("\n--- Endereço Encontrado ---")
        print(f"CEP: {dados.get('cep', 'N/A')}")
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade: {dados.get('localidade', 'N/A')}")
        print(f"Estado: {dados.get('uf', 'N/A')}")
        print("---------------------------\n")

    except requests.exceptions.HTTPError as e:
        print(f"Erro na requisição: O CEP '{cep}' parece ter um formato inválido. Por favor, verifique.")
    except requests.exceptions.RequestException as e:
        # Captura outros erros de conexão (ex: sem internet)
        print(f"Ocorreu um erro de conexão: {e}")
    except ValueError:
        # Erro caso a resposta não seja um JSON válido
        print("A resposta recebida da API não está no formato esperado.")

if __name__ == "__main__":
    # Solicita ao usuário que digite o CEP
    cep_usuario = input("Digite o CEP que deseja consultar (apenas números): ")
    consultar_cep(cep_usuario)