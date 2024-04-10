# Não consegui fazer a parte final de ao finalizar os produtos, reiniciar e só terminar o programa quando apertar "-1"

# Procurei até respostas no ChatGPT e Copilot pra auxílio e mesmo assim não encontrei uma forma do jeito que foi pedida pra realizar a questão.


print('Lojas Tajabara')

i = 1
total = 0
valor = None


while valor != 0:
    valor = float(input(f'Digite o valor do produto {i}'))
    produto = f'Produto {i}: R${valor:.2f}'
    
    total += valor
    print(produto)
    print(f'R${total:.2f}')
    i += 1

dinheiro = float(input('Com quanto você quer pagar?'))
troco = dinheiro - total

if dinheiro < total:
    print('Você não tem dinheiro o suficiente')
else:
    print(f'Seu troco é de: R${troco:.2f}')



