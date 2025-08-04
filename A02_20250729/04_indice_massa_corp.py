l_peso = float(input("Digite seu peso: "))
l_altura = float(input("Digite sua altura: "))
l_imc = l_peso / (l_altura * l_altura)

print("Seu Indice de Massa Corporal eh: ", l_imc)

if l_imc < 18.5:
    print("Voce esta abaixo do peso considerado normal")
elif l_imc > 24.9:
    print("Voce esta acima do peso considerado normal")
else:
    print("Voce esta dentro do indice considerado normal")