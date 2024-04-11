n = int(input('Digite um número: '))
x=1


for i in range(1, n+1, 2):
    print(i)

print('---------------------------')

while x <= n:
    print(x)
    x+=2


print('---------------------------')

for i in range(1, n+1):
    if i % 2 == 0:
        continue
    print(i)
