import csv

def ler_csv(caminho_arquivo: str):
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)


ler_csv("dados.csv")
