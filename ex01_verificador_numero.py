# Exercício 01 - Verificador de Número (Fácil)
# Objetivo: dizer se um número inteiro é positivo, negativo ou zero.

# input() sempre devolve texto; int() converte para número inteiro.
numero = int(input("Digite um número inteiro: "))

# Os três casos são excludentes (um número só pode ser um deles),
# então usamos uma única cadeia if / elif / else.
if numero > 0:
    print("O número é positivo.")
elif numero < 0:
    print("O número é negativo.")
else:
    # Se não é > 0 e não é < 0, só resta ser 0.
    print("O número é nulo (zero).")
