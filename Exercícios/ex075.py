# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9.
# Em que posição foi digitado o primeiro 3.
# Quais foram os números pares.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
tupla = (n1, n2, n3, n4)
print(tupla)
print(f'O 9 apareceu {tupla.count(9)} vezes')
if 3 not in tupla:
    print('O 3 não apareceu em nenhuma posição')
else:
    print(f'O 3 apareceu primeiramente na {tupla.index(3)+1}ª posição ')
print('Os valores pares digitados foram: ', end='')
for c in tupla:
    if c % 2 == 0:
        print(f'{c} ', end='')
