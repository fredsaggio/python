import math as m

numero_usuario = int(input('Digite um número.'))

for i in range(numero_usuario, 1, -1):
    numero_usuario *= i - 1  
    
    # Isso funciona porque "i" para em valor = 2, já que o "1" ali no "fim" não entra no range, só vai até o 2, fazendo "i - 1" ser igual a 1 e o código funcionar, caso contrário "i - 1" seria igual a 0, zerando o cálculo e dando erro.

print(numero_usuario)



# Segunda forma utilizando a biblioteca "math": 

numero_usuario_2 = int(input('Digite um número.'))
fatorial_numero = m.factorial(numero_usuario_2)

print(fatorial_numero)