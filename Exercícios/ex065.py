# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.

maior = menor = soma = cont = 0
parar = 'S'
while parar in 'Ss':
    n = int(input('Digite um número: '))
    parar = str(input('Quer continuar a digitar valores: [S/N] ')).upper().strip()[0]
    if cont == 0:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    cont += 1
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
print('A média entre todos os {} valores vale {:.2f}'.format(cont, soma/cont))
