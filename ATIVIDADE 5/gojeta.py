def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


valor = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))
print(f"O valor da gorjeta é: R$ {calcular_gorjeta(valor, porcentagem):.2f}")
