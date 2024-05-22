tupla = ['amor', 'abraço', 'prato', 'tomada', 'rosa', 'bolsa']
string = input('Digite uma palavra: ')
incluso = False

for i in tupla:
    if string == i:
        print('Está dentro da tupla.')
        incluso = True
        break

if not incluso:
    print('Não está dentro da tupla.')
