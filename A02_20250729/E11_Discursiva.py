l_nota = float(input("Digite a nota do aluno (0 a 10): "))
l_frequencia = float(input("Digite a frequência do aluno (em %): "))


if l_nota >= 6.0 and l_frequencia >= 75.0:
    print("Aluno Aprovado ")
else:
    print("Aluno Reprovado")



#1. Por que o uso do operador lógico and é necessário nessa situação?
#Porque ambas as condições precisam ser verdadeiras ao mesmo tempo para o aluno ser aprovado:
# - A nota do aluno deve ser maior ou igual a 6.0 e a frequência precisa ser igual ou maior que 75%
#O operador and garante que as duas exigências sejam cumpridas simultaneamente. 
#Se uma delas falhar, o aluno deve ser reprovado. Esse é o comportamento ideal para uma regra de aprovação com múltiplos critérios obrigatórios.

#2. O que aconteceria se fosse usado or no lugar de and?
#Se usássemos or, o código ficaria assim:

#if nota >= 6.0 or frequencia >= 75.0:
#    print("Aluno Aprovado")
#else:
#    print("Aluno Reprovado")
#Nesse caso, bastaria que uma das condições fosse verdadeira para o aluno ser aprovado.