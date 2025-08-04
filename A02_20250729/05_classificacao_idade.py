l_idade = float(input("Informe sua idade: "))

if l_idade <= 12:
    print("Crianca")
elif l_idade <= 17:
    print("Adolescente")
elif l_idade <= 59:
    print("Adulto")
else:
    print("Idoso")