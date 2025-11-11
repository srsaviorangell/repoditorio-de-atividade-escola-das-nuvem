import csv

def escrever_csv(caminho_arquivo: str):
    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome", "Idade", "Cidade"])
        escritor.writerow(["Savio", 27, "Belo Horizonte"])
        escritor.writerow(["Ana", 30, "São Paulo"])
        escritor.writerow(["Carlos", 22, "Rio de Janeiro"])

    print("Arquivo CSV criado com sucesso!")


escrever_csv("dados.csv")
