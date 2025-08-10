

def gerar_perfil_usuario():
    """
    Busca um perfil de usuário aleatório da API 'Random User Generator'
    e exibe o nome, email e país.
    """
    # URL da API para obter um usuário aleatório
    url = "https://randomuser.me/api/"

    try:
        # Faz a requisição GET para a API
        resposta = requests.get(url)

        # Verifica se a requisição foi bem-sucedida (código de status 200)
        resposta.raise_for_status()

        # Converte a resposta em formato JSON para um dicionário Python
        dados = resposta.json()

        # Extrai o primeiro resultado da lista de usuários
        usuario = dados['results'][0]

        # Extrai as informações desejadas do perfil do usuário
        nome_completo = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        # Exibe as informações de forma organizada
        print("--- Perfil de Usuário Gerado ---")
        print(f"Nome: {nome_completo}")
        print(f"Email: {email}")
        print(f"País: {pais}")
        print("--------------------------------")

    except requests.exceptions.RequestException as e:
        # Captura e exibe erros de conexão ou HTTP
        print(f"Ocorreu um erro ao conectar-se à API: {e}")
    except (KeyError, IndexError):
        # Captura erros caso a estrutura do JSON seja inesperada
        print("Não foi possível processar os dados recebidos da API.")

if __name__ == "__main__":
    gerar_perfil_usuario()