# Faça um programa que leia um ângulo qualquer e mostre o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do ângulo: '))
radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)
print("""A partir do ângulo de {}, temos: 
SENO igual a {:.2f}, 
COSSENO igual a {:.2f} e 
TANGENTE igual a {:.2f}""".format(angulo, seno, cosseno, tangente))
