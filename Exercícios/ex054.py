# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
# Maioridade : 21 anos

from datetime import date
cont = 0
cont2 = 0
for c in range(1, 8):
    nascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = (date.today().year - nascimento)
    if idade < 21:
        cont += 1
    else:
        cont2 += 1
print('{} pessoas ainda não atingiram a maioridade'.format(cont))
print('{} pessoa atingiram a maioridade'.format(cont2))
