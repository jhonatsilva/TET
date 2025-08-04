l_peso = float(input("Digite seu peso em kg: "))
l_altura = float(input("Digite sua altura em metros: "))
l_imc = l_peso / (l_altura ** 2)    

print(f"Seu Índice de Massa Corporal (IMC) é: {l_imc:.2f}")

if l_imc < 18.5:
    print("Classificação: Abaixo do peso")  
elif 18.5 <= l_imc < 24.9:
    print("Classificação: Peso normal")             
elif 25 <= l_imc < 29.9:
    print("Classificação: Sobrepeso")
elif 30 <= l_imc < 34.9:        
    print("Classificação: Obesidade grau 1 (moderada)")
elif 35 <= l_imc < 39.9:
    print("Classificação: Obesidade grau 2 (severa)")
else:
    print("Classificação: Obesidade grau 3 (mórbida)")
