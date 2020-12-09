# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    lista.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if 'N' in continuar:
        break
    print('=-'*20)
print(f'Dentro de {lista}, existem: ')
print(f'{par} como números pares')
print(f'e {impar} como números ímpares')

"""for i, v in enumerate(n):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)"""