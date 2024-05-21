# Faça um programa que deve receber uma matriz do usuário e printar ao fim a soma de cada coluna da matriz recebida. O usuário primeiro deve entrar com as dimensões (linhas e colunas da matriz) e então alimentar o números de cada linha.

linhas = int(input('Quantas linhas: '))
colunas = int(input('Quantas colunas: '))
matriz = []

for i in range(linhas):
    adicionar = []
    for x in range(colunas):
        coluna = int(input(f'Digite o {x+1}° número da {i+1}° linha: '))
        adicionar.append(coluna)
    matriz.append(adicionar)

print(matriz)