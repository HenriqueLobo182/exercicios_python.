# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a RS1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, aumento é de 15%

salario = float(input('Digite seu salário: R$'))

if salario > 1250.0:
    print('O salário com o aumento de 10%, ficará R${:.2f}'.format(salario*1.1))
else:
    print('O salário com o aumento de 15%, ficará R${:.2f}'.format(salario*1.15))
