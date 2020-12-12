# Aprimore o desafio anterior, mostrando no final:
# A soma de todos os valores pares digitados.
# A soma dos valores da terceira coluna.
# O maior valor da segunda linha.

linha1 = []
linha2 = []
linha3 = []
par = maior = soma = 0
for c in range(0, 9):
    n = int(input('Digite um número: '))

    if n % 2 == 0:  # soma valores pares
        par += n

    if c == 2 or c == 5 or c == 8:  # soma terceira coluna
        soma += n

    if c < 3:
        linha1.append(n)

    elif c <= 5:
        linha2.append(n)
        if c == 3:  # maior da segunda linha
            maior = n
        else:
            if n > maior:
                maior = n

    elif c >= 5:
        linha3.append(n)

print('~'*40)
for l1 in linha1:
    print(f'[{l1:^5}]', end='')
print()
for l2 in linha2:
    print(f'[{l2:^5}]', end='')
print()
for l3 in linha3:
    print(f'[{l3:^5}]', end='')
print()

print('~'*40)
print(f'A soma dos valores pares: {par}')
print(f'Soma terceira coluna: {soma}')
print(f'O maior da segunda linha: {maior}')


print('=-'*20)  # OU


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('~'*40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('~'*40)
print(f'Soma pares: {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'Soma terceira coluna: {scol}')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'Maior segunda linha: {mai}')
