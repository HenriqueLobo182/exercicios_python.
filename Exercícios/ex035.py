# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

t = ((r1+r2) > r3 and (r2+r3) > r1 and (r3+r1) > r2)  # condição para existência de triângulo
if t:
    print('As retas {}, {} e {} podem formar um triângulo'.format(r1, r2, r3))
else:
    print('As retas {}, {} e {} não podem formar um triângulo'.format(r1, r2, r3))
