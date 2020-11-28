# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

from random import choice
aluno01 = str(input('Aluno 1: '))
aluno02 = str(input('Aluno 2: '))
aluno03 = str(input('Aluno 3: '))
aluno04 = str(input('Aluno 4: '))
alunos = [aluno01, aluno02, aluno03, aluno04]
escolhido = choice(alunos)
print('{} deverá apagar o quadro'.format(escolhido))
