# Exercício 08 - Sistema de Entrada em Evento (Difícil)

idade = int(input("Digite a idade: "))
tem_ingresso = input("Possui ingresso? (sim/não): ").lower() == "sim"
vip = input("É VIP? (sim/não): ").lower() == "sim"
horario = int(input("Horário de chegada (0 a 23): "))

# Ordem: primeiro os "vetos", condições que anulam todas as outras.
# 1) Menor de 16 anos tem a entrada negada mesmo com ingresso.
# 2) Sem ingresso, a entrada é negada.
# Só depois disso faz sentido perguntar se é VIP ou qual o horário.
if idade < 16:
    resultado = "Entrada negada"
elif not tem_ingresso:
    resultado = "Entrada negada"
elif vip:
    resultado = "Entrada VIP"
elif horario > 22:
    # "Após 22h" interpretado como estritamente depois das 22h.
    # Se 22h também contar, troque por: horario >= 22
    resultado = "Entrada excepcional (sujeita a lateral)"
else:
    resultado = "Entrada comum"

print(f"Resultado: {resultado}")
