matriz = [[1, 2, 4, 7], [1, 2, 3, 11], [2, 4, 5]]

matriz_ordenada = sorted(matriz, key=lambda linha: (sum(linha), -len(linha)))

print("Matriz original:", matriz)
print("Matriz ordenada:", matriz_ordenada)