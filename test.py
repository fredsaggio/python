with open("arquivo.txt", "w", encoding="utf-8") as arquivo:
    content = arquivo.write("Olá, mundo! Este é um arquivo texto UTF-8 criado usando Python.")

with open("arquivo.txt", "r", encoding='utf-8') as arquivoLer: 
    contentLer = arquivoLer.read()

print(contentLer)