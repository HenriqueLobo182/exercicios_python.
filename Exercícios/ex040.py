# Faça um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida.
# Média abaixo de 5,0 : REPROVADO
# Média entre 5,0 e 6,9 : RECUPERAÇÃO
# Média de 7,0 ou superior: APROVADO

colors = {'red': '\033[31m', 'yellow': '\033[33m', 'green': '\033[32m', 'clean': '\033[m'}
grade01 = float(input('First grade: '))
grade02 = float(input('Second grade: '))

average = (grade01 + grade02) / 2

if average < 5.0:
    print(f'His average was {average:.1f} points')
    print(f'{colors["red"]}FAILED{colors["clean"]}')
elif 5.0 <= average < 7.0:
    print(f'His average was {average:.1f} points')
    print(f'{colors["yellow"]}RETAKE{colors["clean"]}')
else:
    print(f'His average was {average:.1f} points')
    print(f'{colors["green"]}APPROVED{colors["clean"]}')
