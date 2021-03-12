# Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angle = float(input('Type the value of the angle: '))
radian = radians(angle)
sine = sin(radian)
cosine = cos(radian)
tangent = tan(radian)
print(f'From the {angle} degree angle, we have:')
print(f'Sine equal to {sine:.2f}')
print(f'Cosine equal to {cosine:.2f}')
print(f'Tangent equal to {tangent:.2f}')
