# Essa eu quebrei cabeça viu, namoral, usei o chatGPT nessa pra auxílio por conta de algumas partes que não estava compreendendo e acabei abrindo os olhos pra mais coisas até nas outras questões. 

# OBS: Não copiei código do chatGPT, só foi pra ter uma ideia mesmo. 

numero_usuario = int(input('Digite um número.'))

soma_total = 0
frase_serie = ""

for i in range(1, numero_usuario + 1):
    valor = int('2' * i)
    soma_total += valor
    frase_serie += str(valor)
    if i < numero_usuario:
        frase_serie += " + "

print(f'{frase_serie} = {soma_total}')