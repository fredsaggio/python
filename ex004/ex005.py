# Nessa eu fiz 99% correto, só tive dúvida em como fazer o número menor ser colocado na variável, de resto fiz tudo tranquilamente.

# Pra parte do "menor", usei o chatGPT como auxílio só no "menor == 0", no qual eu não percebi que podia colocar essa condição, de resto eu fiz tudo.

n = int(input('Digite um número.'))
soma = 0
menor = 0
maior = 0

for i in range(1, n+1):
    num = int(input(f'Digite o {i} número'))
    soma += num

    if maior == 0 or num >= maior:
        maior = num
        
    if menor == 0 or num <= menor:
        menor = num

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
print(f'A soma dos números: {soma}')