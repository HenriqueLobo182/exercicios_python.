# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = ('Pão', 9.90, 'Leite', 3.50, 'Frango', 10.99, 'Espinafre', 2.89, 'Panetone', 6.10, 'Granola', 12.99)
print('-'*30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*30)

for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<23}', end='')
    else:
        print(f'R${listagem[c]:>5.2f}')
print('-'*30)
