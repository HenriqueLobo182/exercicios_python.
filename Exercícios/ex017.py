# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot
oposto = float(input('Informe o cateto oposto: '))
adjacente = float(input('Informe o cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('A hipotenusa desse triângulo retângulo vale {:.2f}'.format(hipotenusa))
