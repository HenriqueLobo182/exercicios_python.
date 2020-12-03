# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço FOR.

num = int(input('Digite um número: '))
vezes = int(input('Quantas vezes quer multiplicar o número {}? '.format(num)))

for c in range(1, vezes+1):
    print('{} x {:2} = {}'.format(num, c, (num*c)))

print('=-'*20)  # OU

n = int(input('Digite um número: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(n, c, (n*c)))
