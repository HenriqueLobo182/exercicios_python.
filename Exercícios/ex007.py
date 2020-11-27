# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite uma nota: '))
n2 = float(input('Digite outra nota: '))
m = (n1+n2)/2
print('A primeira nota foi {:.1f} e a segunda {:.1f}'.format(n1, n2))
print('A média entre elas será de {:.1f} pontos'.format(m))
