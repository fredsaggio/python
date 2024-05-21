# Faça um programa que diga as dimensões de uma matriz

matriz = [[1, 2, 3], [1, 2, 3, 4 , 5]]
dimensoes = []

num_linhas = len(matriz)
num_colunas = max(len(linha) for linha in matriz)

dimensoes.append(num_linhas)
dimensoes.append(num_colunas)

print(f'Linhas: {num_linhas}')
print(f'Colunas: {num_colunas}')
