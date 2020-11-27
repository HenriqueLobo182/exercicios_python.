# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n*2
t = n*3
rq = pow(n, 1/2)
print('Analisando o valor {} temos que \nSeu dobro será {} \nSeu triplo será {} \ne sua raiz quadrada será {:.2f}.'
      .format(n, d, t, rq))
