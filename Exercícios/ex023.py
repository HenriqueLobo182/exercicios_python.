# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
# Exemplo: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

number = int(input('Type a number: '))
units = number // 1 % 10
dozens = number // 10 % 10
hundreds = number // 100 % 10
thousands = number // 1000 % 10
print(f'Analyzing the number {number}, we have:')
print(f'Units = {units}')
print(f'Dozens = {dozens}')
print(f'Hundreds = {hundreds}')
print(f'Thousands = {thousands}')
