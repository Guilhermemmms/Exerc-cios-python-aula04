# Exercício 07 - Sistema de Benefícios (Difícil)

idade = int(input("Digite a idade do candidato: "))
estudante = input("É estudante? (sim/não): ").lower() == "sim"
empregado = input("É empregado? (sim/não): ").lower() == "sim"
cadastro_ativo = input("Cadastro ativo? (sim/não): ").lower() == "sim"

# A regra 1 é mais exigente que a 2, então vem antes.
# Os parênteses em (empregado or cadastro_ativo) são obrigatórios:
# sem eles, o Python leria (idade < 25 and empregado) or cadastro_ativo,
# o que mudaria o significado da regra.
if idade < 25 and estudante and cadastro_ativo:
    resultado = "Benefício integral"
elif idade < 25 and (empregado or cadastro_ativo):
    resultado = "Benefício parcial"
elif idade >= 25 and cadastro_ativo:
    resultado = "Benefício parcial"
else:
    resultado = "Sem benefício"

print(f"Resultado: {resultado}")
