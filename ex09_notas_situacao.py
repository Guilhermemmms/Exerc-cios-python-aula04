# Exercício 09 - Análise de Notas e Situação do Aluno (Difícil)


def ler_nota(rotulo):
    """Pede uma nota e só aceita valores entre 0 e 10.

    Repete a pergunta até o usuário digitar um valor válido.
    """
    while True:
        valor = float(input(rotulo))
        if 0 <= valor <= 10:
            return valor  # return encerra a função e sai do laço
        print("Nota inválida! Digite um valor entre 0 e 10.")


n1 = ler_nota("Digite a nota N1: ")
n2 = ler_nota("Digite a nota N2: ")
n3 = ler_nota("Digite a nota N3: ")

# A média precisa ser calculada antes de aplicar as regras.
media = round((n1 + n2 + n3) / 3, 2)

if media >= 7.0:
    situacao = "Aprovado"
elif media >= 5.0:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
