nome = input("Nome do vendedor: ")
salario_fixo = float(input("Salário fixo: R$ "))
total_vendas = float(input("Total de vendas no mês: R$ "))

comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_receber:.2f}")
