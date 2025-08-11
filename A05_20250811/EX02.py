l_nome = ["Ana", "Amanda", "Irene", "Maria", "Marcia"]

for i in range(5, 10):
    nome = input(f'Digite o {i + 1}º nome: ')
    l_nome.append(nome) 

for i in range(0, 10):
    print(f'{i + 1}º nome = {l_nome[i]}')
