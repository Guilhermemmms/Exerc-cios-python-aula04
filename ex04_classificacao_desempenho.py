# Exercício 04 - Classificação de Desempenho (Médio)

nota = float(input("Digite a nota do aluno (0 a 10): "))
frequencia = float(input("Digite a frequência do aluno (0 a 100): "))

# A ordem importa: da regra mais restritiva para a mais ampla.
# "Excelente" e "Bom" exigem as duas condições (and).
# "Regular" exige só uma das duas (or), por isso vem por último;
# se viesse antes, capturaria alunos que deveriam ser Excelente ou Bom.
if nota >= 9 and frequencia >= 90:
    resultado = "Excelente"
elif nota >= 7 and frequencia >= 75:
    resultado = "Bom"
elif nota >= 5 or frequencia >= 75:
    resultado = "Regular"
else:
    resultado = "Insuficiente"

print(f"Desempenho: {resultado}")

# Observação: na tabela de exemplos do enunciado, a linha
# "nota 5,0 / frequência 70 -> Insuficiente" contradiz a regra escrita
# (5 >= 5 já torna a regra "Regular" verdadeira). Este código segue a regra.
