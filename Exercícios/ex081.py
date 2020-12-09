# Crie um programa que vai ler vários números e colocar e uma lista. Depois disso, mostre:
# Quantos números foram digitados.
# A lista de valores, ordenada de forma decrescente.
# Se o valor 5 foi digitdo e está ou não na lista.

lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if 'N' in continuar:
        break
    print('=-'*20)
print('~'*30)
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Lista decrescente: {lista}')
if 5 in lista:
    print('O número 5 foi encontrado na lista')
else:
    print('O número 5 não foi encontrado na lista')
