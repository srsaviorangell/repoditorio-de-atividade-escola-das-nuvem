produto = "Camiseta"
preco_original = 50.00
desconto_percentual = 20

valor_desconto = preco_original * desconto_percentual / 100
preco_final = preco_original - valor_desconto

print(f"Produto: {produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto_percentual}% (R$ {valor_desconto:.2f})")
print(f"Preço Final: R$ {preco_final:.2f}")
