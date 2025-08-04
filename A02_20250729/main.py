print("hello world")
sub = 5-1
som = 2 + 3
div = 6/2
mult = 2*4

equ = 1500 + ((1500*5)/100)

print('subtracao: ',sub)
print('soma: ', som)
print('divisao: ', div)
print('multiplicacao: ', mult)
print('equacao: ', equ)

nome = input("Digite seu nome: ")
print("Bem vindo ", nome)

nota1 = float(input("Digite sua nota 1: "))
print("Nota digitada:", nota1)

nota2 = float(input("Digite sua nota 2: "))
print("Nota digitada:", nota2)

media = (nota1 + nota2) / 2

if media >= 60:
    print("Aluno aprovado, média:", media)
else:
    print("Aluno reprovado, média:", media)

