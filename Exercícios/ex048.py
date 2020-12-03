# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no
# intervalo de 1 até 500.

s = 0
cont = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        cont += 1
        s += c
print('A soma entre os {} valores indicados corresponde a {}'.format(cont, s))
