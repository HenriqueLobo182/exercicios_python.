# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date

year_of_birth = int(input('Digite o ano de nascimento do atleta: '))  
age = (date.today().year - year_of_birth)  

if age <= 9:
    print('O atleta tem {} anos'.format(age))
    print('Classificação: MIRIM')
elif 9 < age <= 14:
    print('O atleta tem {} anos'.format(age))
    print('Classificação: INFANTIL')
elif 14 < age <= 19:
    print('O atleta tem {} anos'.format(age))
    print('Classificação: Junior')
elif 19 < age <= 25:
    print('O atleta tem {} anos'.format(age))
    print('Classificação: SÊNIOR')
else:
    print('O atleta tem {} anos'.format(age))
    print('Classificação: MASTER')
