# Exercício 05 - Validador de Login (Médio)

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

# Comparamos texto com ==. Python diferencia maiúsculas de minúsculas.
# Cada combinação válida exige usuário E senha corretos (and).
if usuario == "admin" and senha == "1234":
    print("Acesso administrativo")
elif usuario == "aluno" and senha == "unifecaf":
    print("Acesso autorizado")
else:
    print("Acesso negado")
