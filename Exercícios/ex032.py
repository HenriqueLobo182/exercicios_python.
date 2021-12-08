# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

from datetime import date

year = int(input('Type a year: [0 for the current year] '))

if year == 0: 
    year = date.today().year

circumstance01  = (year % 4 == 0) and (year % 100 != 0)
circumstance02 = (year % 400 == 0)

if circumstance01 or circumstance02:
    print(f'The year {year} is a leap year')
else:
    print(f'The year {year} is not a leap year')
