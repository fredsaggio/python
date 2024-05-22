dicionario = {'salario1': 15000, 'salario2': 20000, 'salario3': 10000, 'salario4': 50000, 'salario5': 2000, 'salario6': 1400, 'salario7': 1800, 'salario8': 8000, 'salario9': 4000}

maior = 0
menor = 0
soma = 0

for i in dicionario.values():
    soma += i
    if i >= maior:
        maior = i
    
    if menor == 0 or i <= menor:
        menor = i

media = soma / 9

print(f'Maior salário: R${maior}')
print(f'Menor salário: R${menor}')
print(f'Média dos salários: R${media:.2f}')