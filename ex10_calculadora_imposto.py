# Exercício 10 - Calculadora de Imposto de Renda Simplificada (Difícil)

salario_bruto = float(input("Digite o salário bruto (R$): "))

# As faixas são definidas como "até X", então testamos do menor teto
# para o maior. Cada elif só é avaliado se o salário passou do teto anterior.
if salario_bruto <= 2259.20:
    aliquota, parcela_deduzir = 0, 0.00
elif salario_bruto <= 2826.65:
    aliquota, parcela_deduzir = 7.5, 169.44
elif salario_bruto <= 3751.05:
    aliquota, parcela_deduzir = 15, 381.44
elif salario_bruto <= 4664.68:
    aliquota, parcela_deduzir = 22.5, 662.77
else:
    aliquota, parcela_deduzir = 27.5, 896.00

# imposto = salário x alíquota - parcela a deduzir
imposto_renda = (salario_bruto * aliquota / 100) - parcela_deduzir
salario_liquido = salario_bruto - imposto_renda

print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Alíquota aplicada: {aliquota}%")
print(f"Imposto de renda: R$ {imposto_renda:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")

# ----- Desafio extra: desconto de INSS -----
# 11% do salário bruto, limitado a R$ 908,85. min() escolhe o menor valor.
inss = min(salario_bruto * 0.11, 908.85)
salario_liquido_final = salario_liquido - inss

print("\n--- Com desconto de INSS (desafio extra) ---")
print(f"Valor do INSS: R$ {inss:.2f}")
print(f"Imposto de renda: R$ {imposto_renda:.2f}")
print(f"Salário líquido final: R$ {salario_liquido_final:.2f}")

# Observação: na tabela de exemplos do enunciado, o salário de 2.500,00
# aparece com imposto de 17,06, mas a conta correta é
# 2500 * 0,075 - 169,44 = 18,06. Este código calcula 18,06.
