def calcular_preco_com_desconto(preco_original: float, percentual_desconto: float) -> float:
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return round(preco_final, 2)


preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto (%): "))
print(f"O preço final com desconto é: R$ {calcular_preco_com_desconto(preco, desconto):.2f}")
