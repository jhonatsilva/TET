valor1 = float(input("Digite o primeiro valor decimal: "))
valor2 = float(input("Digite o segundo valor decimal: "))

media = (valor1 + valor2) / 2

print(f"A média entre {valor1} e {valor2} é {media:.2f}")


# 1. Por que é necessário usar a função float() no input()?
# O input() sempre retorna valores como texto (string).
# Para realizar cálculos matemáticos, é necessário converter esses textos para números.
# A função float() converte a string digitada para um número decimal (ponto flutuante).

# 2. O que aconteceria se fosse feita a soma de duas strings ao invés de dois números?
# Se somássemos duas strings, o Python faria uma concatenação, e não uma soma matemática.
# Exemplo: input1 = "5", input2 = "3" -> input1 + input2 = "53" (texto).
# Portanto, sem a conversão para float, o cálculo da média não funcionaria corretamente.
