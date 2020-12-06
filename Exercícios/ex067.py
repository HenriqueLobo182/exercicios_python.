# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado foi negativo.

while True:
    c = 0
    print('='*40)
    n = int(input('Digite um valor e veja sua tabuada: '))
    print('='*40)
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
print('FIM')
