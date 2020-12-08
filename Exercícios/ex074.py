# Crie um programa que vai gerar números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import choice
lista = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
maior = menor = ''
while True:
    for c in range(1, 6):
        ec = choice(lista)
        if c == 1:
            print(f'Foram sorteados os valores: {ec}', end=' ')
            maior = ec
            menor = ec
        else:
            print(f'{ec}', end=' ')
            if ec > maior:
                maior = ec
            if ec < menor:
                menor = ec
    else:
        break
print(f'\nO maior foi {maior}')
print(f'O menor foi {menor}')

print('=-'*20)  # OU

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Foram sorteados os valores: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior foi {max(numeros)}')
print(f'O menor foi {min(numeros)}')
