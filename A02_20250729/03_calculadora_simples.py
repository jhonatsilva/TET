numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))

l_soma = numero1 + numero2
l_subtr = numero1 - numero2
l_mult = numero1 * numero2

if numero2 == 0:
    l_div = ("valor ", numero2, "invalido, nao eh possivel dividir por zero")
else:
    l_div = numero1/numero2

print("soma: ", l_soma)
print("subtracao: ", l_subtr)
print("multiplicacao: ", l_mult)
print("divisao: ", l_div)