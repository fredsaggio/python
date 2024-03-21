palavra1 = input('Digite uma palavra');
palavra2 = input('Digite outra palavra');
inteiro = int(input('Digite um inteiro')); # Declarar em int() pra funcionar o codigo, estava dando erro.


print(palavra1 + palavra2);
print(palavra1, palavra2, sep="\n");
print(palavra1 * inteiro, palavra2 * inteiro, (palavra1 + palavra2) * inteiro, sep="");
