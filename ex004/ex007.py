n = int(input('Digite um número.'))
soma = 0
texto = ""

for i in range(0, n):
    termo = (1+i)/(i+(i+1))
    soma += termo
    texto += f"{1+i}/{(i+(i+1))}"
    if i < n-1:
        texto += " + "

print(f'{texto} = {soma:.3f}')