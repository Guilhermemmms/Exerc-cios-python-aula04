# Exercício 02 - Par ou Ímpar, com bônus de sinal (Fácil)

numero = int(input("Digite um número: "))

# O operador % devolve o resto da divisão.
# Resto 0 na divisão por 2 significa que o número é par.
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

# Bônus: segundo bloco, independente do primeiro, porque
# "par/ímpar" e "positivo/negativo/zero" são perguntas diferentes.
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número {numero} é zero.")
