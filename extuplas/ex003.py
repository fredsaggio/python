dicionario = {'123': 'carro', '456': 'moto', '789': 'onibus'}
chave = input('Digite uma chave do dicionário: ')
incluso = False

for i in dicionario:
    if chave == i:
        dicionario.pop(chave)
        incluso = True
        print('Chave removida com sucesso.')
        break

if not incluso: 
    print(dicionario.keys())

dicionario2 = {'135': 'bicicleta', '497': 'mobilete', '814': 'avião'}
dicionario.update(dicionario2)

print(dicionario)



    