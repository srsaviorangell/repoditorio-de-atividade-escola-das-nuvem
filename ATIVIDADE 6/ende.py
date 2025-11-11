import requests

def consultar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" not in dados:
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
        else:
            print("CEP não encontrado.")
    else:
        print("Erro na consulta. Verifique a conexão.")

cep = input("Digite o CEP: ")
consultar_cep(cep)
