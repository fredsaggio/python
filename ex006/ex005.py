passar = 6.0
lista_notas = []
lista_passados = []
soma = 0

for i in range(5):
    nota = float(input(f'Digite a nota do {i+1}° aluno: '))
    soma += nota
    lista_notas.append(nota)

for j in lista_notas:
    if j >= passar:
        lista_passados.append(j)
    
media = soma / len(lista_notas)
print(f'A média da nota dos alunos foi de: {media:.2f}, as notas iguais ou acima da média são: {lista_passados}')