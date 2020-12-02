# Faça um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com
# a média atingida.
# Média abaixo de 5,0 : REPROVADO
# Média entre 5,0 e 6,9 : RECUPERAÇÃO
# Média de 7,0 ou superior: APROVADO

cores = {'vermelho': '\033[31m', 'amarelo': '\033[33m', 'verde': '\033[32m', 'limpa': '\033[m'}
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

m = (n1+n2) / 2

if m < 5.0:
    print('Sua média foi de {:.1f} pontos'.format(m))
    print('{}REPROVADO{}'.format(cores['vermelho'], cores['limpa']))
elif 5.0 <= m < 7.0:
    print('Sua média foi de {:.1f} pontos'.format(m))
    print('{}RECUPERAÇÃO{}'.format(cores['amarelo'], cores['limpa']))
else:
    print('Sua média foi de {:.1f} pontos'.format(m))
    print('{}APROVADO{}'.format(cores['verde'], cores['limpa']))
