# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior. O segundo valor é maior. Não existe valor maior, os dois são iguais.

number01 = int(input('Type a number: '))
number02 = int(input('Type another number: '))

if number01 > number02:
    print('The first number is greater!')
elif number02 > number01:
    print('The second number is greater!')
else:
    print('The two are the same, there is no greater number!')
