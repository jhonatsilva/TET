
l_nome = input("Digite o nome do aluno: ")
l_nota1 = float(input("Digite a nota 1: "))
l_nota2 = float(input("Digite a nota 2: "))

l_media = (l_nota1 + l_nota2) / 2

if l_media >= 6:
    print(f"{l_nome} foi aprovado com média {l_media:.2f}.")        
else:
    print(f"{l_nome} foi reprovado com média {l_media:.2f}.")
