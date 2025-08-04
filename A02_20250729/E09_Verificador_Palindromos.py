l_texto = input("Digite uma palavra ou frase: ")

l_texto_formatado = ''.join(c.lower() for c in l_texto if c.isalnum())

if l_texto_formatado ==l_texto_formatado[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
