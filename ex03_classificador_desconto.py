# Exercício 03 - Classificador de Desconto (Médio)

valor_compra = float(input("Digite o valor da compra (R$): "))
idade = int(input("Digite a idade do cliente: "))

# Passo 1: desconto de faixa, conforme o valor da compra.
# As faixas se sobrepõem (600 também é >= 200), então testamos
# da mais alta para a mais baixa. Se começássemos por >= 200,
# uma compra de 600 receberia só 5% em vez de 10%.
if valor_compra >= 500:
    desconto = 10
elif valor_compra >= 200:
    desconto = 5
else:
    desconto = 0

# Passo 2: o desconto por idade é ADICIONAL, não substitui o de cima.
# Por isso é um "if" separado (e não um "elif"): as duas regras
# podem valer ao mesmo tempo.
if idade >= 60:
    desconto = desconto + 5

# Passo 3: aplicar o desconto total sobre o valor da compra.
valor_final = valor_compra - (valor_compra * desconto / 100)

print(f"Desconto aplicado: {desconto}%")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
