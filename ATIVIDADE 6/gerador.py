import random
import string

def gerar_senha(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha


tamanho = int(input("Digite o número de caracteres da senha: "))
print("Sua senha aleatória é:", gerar_senha(tamanho))
