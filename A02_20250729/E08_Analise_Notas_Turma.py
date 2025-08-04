l_qtd_alunos = int(input("Digite a quantidade de alunos: "))

l_notas = []

for i in range(l_qtd_alunos):
    l_nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    l_notas.append(l_nota)

l_media_geral = sum(l_notas) / l_qtd_alunos
l_maior_nota = max(l_notas)
l_menor_nota = min(l_notas)

print(f"\nMédia geral da turma: {l_media_geral:.2f}")
print(f"Maior nota: {l_maior_nota:.2f}")
print(f"Menor nota: {l_menor_nota:.2f}")