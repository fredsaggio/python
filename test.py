while True:
    num = input('digite um número de 1 a 6: ')

    if not num.isnumeric():
        print('Não é número')
        continue

    if int(num) < 1 or int(num) > 6:
        print('inválido')