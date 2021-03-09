# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

number01 = float(input('Type a note: '))
number02 = float(input('Type another note: '))
average = (number01 + number02) / 2
print(f'The first note is worth {number01} and the second is worth {number02}')
print(f'The average between them is worth {average:.2f}')
