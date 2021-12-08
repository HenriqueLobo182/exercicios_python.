# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a RS1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, aumento é de 15%

salary = float(input('Type your salary: R$'))

if salary > 1250.0:
    salaryIncrease = salary * 1.1
    print(f'The salary with the 10% increase, will be {salaryIncrease:.2f}')
else:
    salaryIncrease = salary * 1.15
    print(f'The salary with the 15% increase, will be {salaryIncrease:.2f}')
