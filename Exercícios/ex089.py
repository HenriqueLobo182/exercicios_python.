# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permite que o usuário pessoa mostras as notas de cada aluno individualmente.

aluno = []

while True:
    cadastro = []
    nome = str(input('Nome aluno: '))
    n1 = float(input(f'1ª nota de {nome}: '))
    n2 = float(input(f'2ª nota de {nome}: '))
    media = (n1+n2) / 2
    cadastro.append(nome)
    cadastro.append(n1)
    cadastro.append(n2)
    cadastro.append(media)
    aluno.append(cadastro[:])

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if 'N' in continuar:
        print('~' * 40)
        break

    print('~'*40)

print(f'| {"Cadastro":<} | {"Aluno":^12} | {"Média":^5} |')
for c, a in enumerate(aluno):
    print(f'| {c:^8} | {aluno[c][0]:^12} | {aluno[c][3]:^5.1f} |')
print('~'*40)

while True:
    nota = int(input(f'Deseja ver a nota de qual aluno [0/{len(aluno) - 1}]? '))
    while -1 >= nota or nota >= len(aluno):  # enquanto o usuário não informar um cadastro válido
        nota = int(input(f'Aluno desconhecido. Tente novamente [0/{len(aluno) - 1}]: '))
    else:
        print(f'{aluno[nota][0]} tirou {aluno[nota][1]} e {aluno[nota][2]}')  # cadastro válido
    print('~'*40)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar mostrando as notas dos alunos [S/N]? ')).upper().strip()[0]
    if 'N' in continuar:
        break
print('FIM')


print('=-'*20)  # OU


ficha = list()
while True:
    nomee = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    mediaa = (nota1+nota2) / 2
    ficha.append([nomee, [nota1, nota2], mediaa])
    resp = str(input('Quer continuar [S/N]? '))
    if resp in 'Nn':
        break
print('~'*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('FIM')
