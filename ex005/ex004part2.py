# Questão 2:

import random as r

while True:
    numero = r.randint(1, 9)
    advinhar = str(input('Tente advinhar o número de 1 a 9: '))

    if not advinhar.isnumeric():
        print('Só números devem ser digitados.')
        continue

    if len(advinhar) >= 2 or int(advinhar) == 0:
        print('O número deve estar entre 1 e 9.')
        continue

    if int(advinhar) == numero:
        print(f'Parabéns, você acertou o número! Era realmente o {advinhar}! :)')
        
    else: 
        print(f'Você errou! O número correto era o {numero} ! :(')
        
