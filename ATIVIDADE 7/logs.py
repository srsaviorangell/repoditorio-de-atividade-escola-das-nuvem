import statistics

def analisar_logs(caminho_arquivo: str):
    tempos = []

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            if "Tempo de execução" in linha:
                tempo = float(linha.split(":")[1].strip())
                tempos.append(tempo)

    if tempos:
        media = statistics.mean(tempos)
        desvio = statistics.stdev(tempos)
        print(f"Média do tempo de execução: {media:.2f}")
        print(f"Desvio padrão: {desvio:.2f}")
    else:
        print("Nenhum dado de tempo encontrado no arquivo.")


analisar_logs("logs.txt")
