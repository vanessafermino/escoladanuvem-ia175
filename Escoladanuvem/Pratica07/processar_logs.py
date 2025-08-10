import pandas as pd

def processar_loogs_treinamento(nome_arquivo):
    try: 
        df = pd.read_csv(nome_arquivo)
        media_tempo = df["tempo_execucao"].mean()
        desvio_padrao_tempo = df["tempo_execucao"].std()
        print(f"Média do tempo de execução: {media_tempo:2f} segundos.")
        print(f"Desvio Padrão do tempo de execução: {desvio_padrao_tempo:2f} segundos.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")    


nome_arquivo = input("Digite o nome do arquivo de log:")
processar_loogs_treinamento(nome_arquivo)