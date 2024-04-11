n = input('Enter a number: ')
soma = 0
n = int(n) # Redeclared variable

while not n.isnumeric(): # Using a 'while' to check errors.
    
    print('Invalid value, enter an integer.')
    n = int(input('Enter a number: '))

for i in range(1, int(n)+1):
    valor = (input(f'Enter the {i}º value: '))

    while len(valor) > 2: # Added to improve the code.
        print('Invalid value, max length = 2.')
        valor = (input(f'Enter the {i}º value: '))

    while not valor.isnumeric():
        print('Invalid value, enter an integer.')
        valor = (input(f'Enter the {i}º value: '))

    soma += int(valor)

total_amount = soma / int(n)

print(f'The average of the amounts received is: {total_amount:.2f}')