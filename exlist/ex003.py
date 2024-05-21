# Escreva um programa para contar em uma lista de stringss quantas têm mais de 2 caracteres e começam e terminam com o mesmo caractere:

lista = ['alemanha', 'oi', 'si', 'linda', 'ouriço', 'au', 'ui']
soma = 0
len_chr = 0
same_chr = 0

for i in lista: 
    soma += 1

    if len(i) > 2:
        len_chr += 1
    
    if i[0] == i[-1]:
        same_chr += 1

print('Strings na lista: {}'.format(soma))
print('Strings com mais de 2 caracteres: {}'.format(len_chr))
print('Strings com o mesmo caractere na primeira e ultima posição: {}'.format(same_chr))


