
def consultar_cotacao(codigo_moeda):
    """
    Consulta a cotação de uma moeda em relação ao BRL usando a AwesomeAPI.
    Exibe o valor atual, máximo, mínimo e a data da última atualização.
    """
    # Garante que o código da moeda esteja em maiúsculas
    codigo_moeda = codigo_moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{codigo_moeda}-BRL"

    try:
        # Faz a requisição para a API
        response = requests.get(url)
        
        # Verifica se a requisição foi bem-sucedida (status code 200)
        # Se o código da moeda for inválido, a API retorna 404
        response.raise_for_status()

        # Converte a resposta em formato JSON
        dados = response.json()
        
        # A chave principal do dicionário é a junção das moedas (ex: 'USDBRL')
        chave_cotacao = f"{codigo_moeda}BRL"
        cotacao = dados[chave_cotacao]

        # Extrai os dados de interesse
        valor_atual = float(cotacao['bid'])
        valor_maximo = float(cotacao['high'])
        valor_minimo = float(cotacao['low'])
        timestamp = int(cotacao['timestamp'])
        
        # Converte o timestamp para um formato de data e hora legível
        data_atualizacao = datetime.fromtimestamp(timestamp).strftime('%d/%m/%Y %H:%M:%S')

        # Exibe os resultados formatados
        print("\n--- Cotação Encontrada ---")
        print(f"Moeda: {cotacao['name']}")
        print(f"Data da Consulta: {data_atualizacao}")
        print("--------------------------")
        print(f"Valor Atual (Compra): R$ {valor_atual:,.4f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"Máxima do Dia: R$ {valor_maximo:,.4f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print(f"Mínima do Dia: R$ {valor_minimo:,.4f}".replace(",", "X").replace(".", ",").replace("X", "."))
        print("--------------------------\n")

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"\nErro: A moeda com o código '{codigo_moeda}' não foi encontrada. Verifique o código e tente novamente.")
        else:
            print(f"\nErro HTTP: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"\nErro de Conexão: Não foi possível se conectar à API. Verifique sua conexão com a internet. ({req_err})")
    except KeyError:
        print("\nErro: Não foi possível processar a resposta da API. O formato dos dados pode ter mudado.")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")

if __name__ == "__main__":
    try:
        codigo = input("Digite o código da moeda para consulta (ex: USD, EUR, GBP): ")
        if not codigo:
            print("Nenhum código foi inserido.")
        else:
            consultar_cotacao(codigo)
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")