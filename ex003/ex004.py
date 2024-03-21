import math as m

nome1 = input('Diga um nome');
nome2 = input('Diga outro nome');

nome1len = m.floor(len(nome1) / 2);
nome2len = m.floor(len(nome2) / 2);

filho = nome1[:nome1len] + nome2[nome2len:];

print(filho);