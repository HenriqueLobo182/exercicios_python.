# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

number01 = int(input('First number: '))
number02 = int(input('Second number: '))
number03 = int(input('Third number: '))

smallest = number01
if number02 < smallest:
    smallest = number02
if number03 < smallest:
    smallest = number03
print(f'The smallest number was {smallest}')

highest = number01
if number02 > highest:
    highest = number02
if number03 > highest:
    highest = number03
print(f'The highest number was {highest}')
