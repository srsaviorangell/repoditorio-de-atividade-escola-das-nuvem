pares = 0
impares = 0

print("Digite números inteiros. Digite 'fim' para encerrar.")

while True:
    entrada = input("Número: ").lower()
    if entrada == "fim":
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Erro: insira um número inteiro válido.")

print(f"\nQuantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
