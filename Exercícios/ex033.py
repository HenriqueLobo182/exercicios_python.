# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

menor = n1  # Verificando quem é o menor
if n2 < n3 and n2 < n1:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor número foi {}'.format(menor))

maior = n1  # Verificando quem é o maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número foi {}'.format(maior))
