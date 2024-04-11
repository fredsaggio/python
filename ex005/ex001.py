palavra = str(input('Digite uma string com letras e números.'))
letras = ''
numeros = ''

for i in range(len(palavra)):
    if palavra[i].isnumeric():
        numeros += palavra[i]
    if not palavra[i].isnumeric():
        letras += palavra[i]

print(letras)
print(numeros)