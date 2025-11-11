import requests

def consultar_cotacao(moeda: str):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"

        if chave in dados:
            info = dados[chave]
            print(f"💵 Moeda: {info['name']}")
            print(f"Valor atual: R$ {info['bid']}")
            print(f"Máximo: R$ {info['high']}")
            print(f"Mínimo: R$ {info['low']}")
            print(f"Atualizado em: {info['create_date']}")
        else:
            print("Moeda não encontrada. Tente USD, EUR, GBP, etc.")
    else:
        print("Erro ao consultar cotação.")

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(moeda)
