# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

number = int(input('Type a number: '))
double = number * 2
triple = number * 3
squareRoot = pow(number, 1 / 2)
print(f'Analysing the value {number}, we have that:')
print(f'your double is worth {double},')
print(f'your triple is worth {triple}')
print(f'and your square root is worth {squareRoot:.2f}')
