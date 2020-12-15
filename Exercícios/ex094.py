# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
# todos os dicionários em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# A média de idade do grupo.
# Uma lista com todos as mulheres.
# Uma lista com todas as pessoas com idade acima da média.

lista = []
qnt = soma = 0
while True:
    dicionario = dict()
    dicionario['nome'] = str(input('Nome: '))
    sexo = str(input(f'Sexo? [F/M] ')).upper().strip()[0]
    while sexo not in 'FM':
        sexo = str(input(f'Sexo? [F/M] ')).upper().strip()[0]
    else:
        dicionario['sexo'] = sexo
    dicionario['idade'] = int(input(f'Idade? '))
    lista.append(dicionario.copy())
    qnt += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if 'N' in continuar:
        break
    print('~'*30)
print(lista)
print('~'*50)
print(f'Foram cadastradas {qnt} pessoas')

for c in range(0, len(lista)):
    soma += lista[c]["idade"]
media = soma / qnt
print(f'A média de idade do grupo foi de {media:5.2f} anos')

print(f'Todas as mulheres: ', end='')
for c in range(0, len(lista)):
    if lista[c]["sexo"] in 'F':
        print(f'[{lista[c]["nome"]}]', end='')
print()

print(f'Pessoas com idade maiores que a média: ', end='')
for c in range(0, len(lista)):
    if lista[c]["idade"] > media:
        print(f'[{lista[c]["nome"]} com {lista[c]["idade"]} anos]', end='')
print()
