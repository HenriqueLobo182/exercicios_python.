# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

an = int(input('Digite seu ano de nascimento: '))  # ano de nascimento
i = (date.today().year - an)  # idade

if i < 18:
    print('Você tem {} anos.'.format(i))
    print('Daqui a {} anos você deverá se alistar'.format(18 - i))
    print('Seu alistamento será em {}'.format(date.today().year + (18 - i)))
elif i > 18:
    print('Você tem {} anos.'.format(i))
    print('O tempo de alistamento foi ultrapassado em {} anos'.format(i - 18))
    print('Seu alistamento deveria ter sido feito em {}'.format(date.today().year - (i - 18)))
else:
    print('Você tem {} anos'.format(i))
    print('{} é o ano do seu alistamento'.format(date.today().year))
