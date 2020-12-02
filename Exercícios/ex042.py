# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero : todos lados iguais.
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.

r1 = float(input('Primeira reta: '))  # primeira reta
r2 = float(input('Segunda reta: '))  # segunda reta
r3 = float(input('Terceira reta: '))  # terceira reta

t = (r1+r2) > r3 and (r1+r3) > r2 and (r2+r3) > r1  # condição existência de um triângulo

if t and r1 == r2 == r3:
    print('As retas {}, {} e {} podem formar um triângulo EQUILÁTERO'.format(r1, r2, r3))
elif t and (r1 == r2 or r1 == r3 or r2 == r3):
    print('As retas {}, {} e {} podem formar um triângulo ISÓSCELES'.format(r1, r2, r3))
elif t and r1 != r2 != r3 != r1:
    print('As retas {}, {} e {} podem formar um triângulo ESCALENO'.format(r1, r2, r3))
else:
    print('As retas {}, {} e {} NÃO podem formar um triângulo'.format(r1, r2, r3))
