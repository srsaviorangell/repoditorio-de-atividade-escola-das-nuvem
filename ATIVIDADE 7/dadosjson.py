import json

def manipular_json(caminho_arquivo: str):
    pessoa = {
        "nome": "Savio",
        "idade": 27,
        "cidade": "Belo Horizonte"
    }

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

    print("Arquivo JSON criado com sucesso!")

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        print("Dados lidos do JSON:")
        print(dados)


manipular_json("pessoa.json")
