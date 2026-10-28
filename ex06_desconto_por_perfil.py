# Exercício 06 - Classificador de Desconto por Perfil (Médio)

valor_compra = float(input("Digite o valor da compra (R$): "))
idade = int(input("Digite a idade do cliente: "))
resposta_estudante = input("O cliente é estudante? (sim/não): ")

# .lower() converte para minúsculas, então "Sim", "SIM" e "sim"
# são tratados do mesmo jeito. O resultado da comparação (True/False)
# fica guardado numa variável para deixar os if mais legíveis.
estudante = resposta_estudante.lower() == "sim"

# Todas as regras formam uma única cadeia (são excludentes).
# A regra mais exigente (and) vem antes da menos exigente (or);
# se o "or" viesse primeiro, quem tem 60+ e compra >= 500
# receberia só 10% em vez de 15%.
if valor_compra >= 500 and idade >= 60:
    desconto = 15
elif valor_compra >= 500 or estudante:
    desconto = 10
elif valor_compra >= 200:
    desconto = 5
else:
    desconto = 0

valor_final = valor_compra - (valor_compra * desconto / 100)

print(f"Desconto aplicado: {desconto}%")
print(f"Valor final da compra: R$ {valor_final:.2f}")
