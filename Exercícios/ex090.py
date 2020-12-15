# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o
# conteúdo da estrutura na tela.

aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif aluno['média'] >= 5:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('~'*30)
for k, v in aluno.items():
    print(f'- {k} igual a {v}')
