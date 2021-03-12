# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

from random import choice
student01 = str(input('Student 1: '))
student02 = str(input('Student 2: '))
student03 = str(input('Student 3: '))
student04 = str(input('Student 4: '))
students = [student01, student02, student03, student04]
chosenStudent = choice(students)
print(f'{chosenStudent} must clean the board')
