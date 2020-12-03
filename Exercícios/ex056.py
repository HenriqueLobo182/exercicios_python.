# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

s = 0
maior = 0
nomevelho = ''
feminino = 'F'
masculino = 'M'
cont = 0
for c in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa (F) ou (M): '.format(c))).upper().strip()
    print('=-'*20)

    # média de idades
    s += idade

    # homem mais velho
    if c == 1 and sexo in 'Mm':
        nomevelho = nome
        maior = idade
    else:
        if idade > maior:
            nomevelho = nome
            maior = idade

    # mulheres menores de 20 anos
    if sexo in 'Ff' and idade < 20:
        cont += 1

print('A média de idade entre as pessoas é de {:.1f} anos'.format(s / 4))
print('{} mulheres possuem menos de 20 anos'.format(cont))
print('Com {} anos, {} é o homem mais velho'.format(maior, nomevelho))
