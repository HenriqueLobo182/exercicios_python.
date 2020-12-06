# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
# se o usuário quer ou não continuar. No final, mostre:
# Quantas pessoas tem mais de 18 anos.
# Quantos homens foram cadastrados.
# Quantas mulheres tem menos de 20 anos.

contidade = conthomem = contmulheres = 0  # contagem de maiores de 18 anos, contagem de homens e contagem de mulheres
# menores de 20 anos

print('=-'*15)
print('CADASTRO DE PESSOAS')
print('=-'*15)

while True:
    idade = int(input(f'Idade da pessoa: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input(f'Sexo da pessoa [M/F]: ')).upper().strip()[0]
    print('='*45)
    if idade >= 18:
        contidade += 1
    if sexo in 'M':
        conthomem += 1
    if sexo in 'F' and idade < 20:
        contmulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a cadastrar pessoas [S/N]? ')).upper().strip()[0]
    if continuar in 'N':
        break

print('~'*45)
print(f'Foram cadastradas {contidade} pessoas maiores de 18 anos')
print(f'Foram cadastrados {conthomem} homens')
print(f'Foram cadastradas {contmulheres} mulheres menores de 20 anos')
