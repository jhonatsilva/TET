l_numero = int(input("Digite um número para gerar a tabuada: "))
l_limite = int(input("Digite até qual número deseja calcular a tabuada: "))

print(f"\nTabuada do {l_numero} até {l_limite}:\n" + "-" * 30)

for i in range(1, l_limite + 1):
    print(f"{l_numero} x {i:>2} = {l_numero * i}")
