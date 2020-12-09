# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

lista = list()
menor = 0
maior = 0
menor_posicao = list()
maior_posicao = list()
for cont in range(0, 5):
    numero = int(input(f'Digite um número na posição {cont}: '))
    if cont == 0:
        menor = numero
        maior = numero
        maior_posicao.append(cont)
        menor_posicao.append(cont)

    elif cont > 0:
        if numero > maior:
            maior_posicao.pop()  # maior valor perde sua posição antiga
            maior_posicao.append(cont)  # novo maior valor recebe nova posição
            maior = numero

        elif numero < menor:
            menor_posicao.pop()  # menor valor perde sua posição antiga
            menor_posicao.append(cont)  # novo menor valor recebe nova posição
            menor = numero

        elif numero == maior:
            maior_posicao.append(cont)

        elif numero == menor:
            menor_posicao.append(cont)

    lista.append(numero)
print(f'{lista} foram os valores digitados.')
print(f'Na posição {f"{menor_posicao}"}, {menor} foi menor valor digitado')
print(f'Na posição {f"{maior_posicao}"}, {maior} foi o maior valor digitado')

print('=-'*30)  # OU

listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor na posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'Você digitou {listanum}')
print(f'O maior foi {mai} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor foi {men} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')
