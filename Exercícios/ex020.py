# O mesmo professor quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
aluno01 = str(input('Aluno 1: '))
aluno02 = str(input('Aluno 2: '))
aluno03 = str(input('Aluno 3: '))
aluno04 = str(input('Aluno 4: '))
alunos = [aluno01, aluno02, aluno03, aluno04]
shuffle(alunos)
print("""A ordem de apresentação será: 
{}""".format(alunos))
