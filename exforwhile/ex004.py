n = int(input('Digite um número: '))

print(f'Tabuada de {n}')

for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')


print('----------------------------')

x = 1
while x <= 10:
    print(f'{n} x {x} = {n*x}')
    x+=1