# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date

an = int(input('Digite o ano de nascimento do atleta: '))  # ano de nascimento
i = (date.today().year - an)  # idade

if i <= 9:
    print('O atleta tem {} anos'.format(i))
    print('Classificação: MIRIM')
elif 9 < i <= 14:
    print('O atleta tem {} anos'.format(i))
    print('Classificação: INFANTIL')
elif 14 < i <= 19:
    print('O atleta tem {} anos'.format(i))
    print('Classificação: Junior')
elif 19 < i <= 25:
    print('O atleta tem {} anos'.format(i))
    print('Classificação: SÊNIOR')
else:
    print('O atleta tem {} anos'.format(i))
    print('Classificação: MASTER')
