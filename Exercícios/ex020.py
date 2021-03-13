# O mesmo professor quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
student01 = str(input('Student 1: '))
student02 = str(input('Student 2: '))
student03 = str(input('Student 3: '))
student04 = str(input('Student 4: '))
students = [student01, student02, student03, student04]
shuffle(students)
print(f"The order of the students' presentation will be: {students}")
