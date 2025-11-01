notas = []

print("Digite as notas dos alunos (0 a 10). Digite 'fim' para encerrar.")

while True:
    entrada = input("Nota: ").lower()
    if entrada == "fim":
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite apenas números ou 'fim'.")

if len(notas) > 0:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")
