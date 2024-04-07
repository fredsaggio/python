n = int(input('Digite um número'))

serie = ""
soma = 0

for i in range(1, n+1):
    termo = int('2' * i)
    soma += termo
    serie += str(termo)
    if i < n: 
        serie += "+"


print(f'{serie} = {soma}')