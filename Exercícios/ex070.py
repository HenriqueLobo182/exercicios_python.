# Crie um programa que leia o nome de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final,
# mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$1000.
# Qual é o nome do produto mais barato.

print('='*30)
print('{:^30}'.format('Supermercado Python'))
print('='*30)
soma = contproduto = c = menor = 0  # valor da compra, quantidade de produtos maiores de R$1000, número de laços no
# while e produto mais barato.
nomemenor = ''
while True:
    nome = str(input('Nome do produto: ')).upper().strip()
    preco = float(input(f'Preço do/da {nome}: R$'))
    print('='*40)
    soma += preco

    if preco > 1000:
        contproduto += 1
    if c == 0 or preco < menor:  # c == 0: primeiro laço no WHILE
        menor = preco
        nomemenor = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar comprando [S/N]? ')).upper().strip()[0]
    if continuar in 'N':
        break
    c += 1
print('~'*40)
print(f'O total da compra foi R${soma:.2f}')
print(f'Foram comprados {contproduto} produtos acima de R$1000,00')
print(f'No valor de R${menor:.2f}, {nomemenor} foi o produto comprado mais barato')
