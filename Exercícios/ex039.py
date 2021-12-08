# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

year_of_birth = int(input('Type your year of birth: '))  
age = (date.today().year - year_of_birth)  

if age < 18:
    years_until_military_enlistment = (18 - age)
    year_of_military_enlistment = (date.today().year + years_until_military_enlistment)
    print(f'You are {age} years old')
    print(f'{years_until_military_enlistment} years from now you need to enlist in the military')
    print(f'Your military enlistment will be in {year_of_military_enlistment}')

elif age > 18:
    years_exceeded = (age - 18)
    year_of_military_enlistment = (date.today().year - years_exceeded)
    print(f'You are {age} years old')
    print(f'The military enlistment period was exceeded by {years_exceeded} years')
    print(f'Your military enlistment should have been done on {year_of_military_enlistment}')

else:
    print(f'You are {age} years old')
    print(f'{date.today().year} is the year of your military enlistment')
