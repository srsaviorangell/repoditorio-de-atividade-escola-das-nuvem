numero_funcionario = int(input("Número do funcionário: "))
horas_trabalhadas = float(input("Horas trabalhadas: "))
valor_por_hora = float(input("Valor por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"Número do funcionário = {numero_funcionario}")
print(f"Salário = R$ {salario:.2f}")
