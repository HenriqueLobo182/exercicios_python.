# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

from datetime import date

ano = int(input('Digite um ano? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

s1 = (ano % 4 == 0) and (ano % 100 != 0)  # situação 1
s2 = (ano % 400 == 0)  # situação 2

if s1 or s2:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
