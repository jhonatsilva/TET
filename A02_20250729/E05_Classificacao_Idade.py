l_idade = int(input("Digite sua idade: "))

if l_idade < 13:
    print("Classificação: Criança")
elif l_idade < 18:
    print("Classificação: Adolescente")
elif l_idade < 60:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")   