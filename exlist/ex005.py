# Faça um programa que selecione um item aleatório da lista: 

import random as r

lista = ['temaki', 'comida', 'japão', 'peixe', 'tinta', 'molho', 'dinheiro', 'camarão']

indice = r.randint(0, len(lista)-1)

print(lista[indice])