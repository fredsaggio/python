import random as r

numero = r.randrange(1, 10)
advinhar = int(input('Tente advinhar o número de 1 a 9: '))

if advinhar == numero:
    print(f'Parabéns, você acertou o número! Era realmente o {advinhar}!')
else: 
    print(f'Você errou! O número correto era o {numero}! :()')