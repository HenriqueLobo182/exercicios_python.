# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]
par = list()
impar = list()
lista[0] = par
lista[1] = impar

for c in range(1, 8):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
par.sort()
impar.sort()
print('~'*30)
print(f'Pares: {par}')
print(f'Ímpares: {impar}')


print('=-'*20)  # OU


num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('~'*30)
num[0].sort()
num[1].sort()
print(f'Pares: {num[0]}')
print(f'Ímpares: {num[1]}')
