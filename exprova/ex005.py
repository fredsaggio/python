numeros = int(input('Digite um número: '))
maior_valor = 0
menor_valor = 0 
soma = 0

for i in range(1, numeros+1):
    numero = int(input(f'Digite o {i}º número: '))
    soma += numero
    if numero >= maior_valor or maior_valor == 0:
        maior_valor = numero
    if numero <= menor_valor or menor_valor == 0:
        menor_valor = numero

print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')
print(f'Soma dos valores: {soma}')