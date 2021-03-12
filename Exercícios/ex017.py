# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot
opposite = float(input('Enter the value of the opposite side: '))
adjacent = float(input('Enter the value of the adjacent side: '))
hypotenuse = hypot(opposite, adjacent)
print(f'The hypotenuse of the right triangle is equal to {hypotenuse:.2f}')
