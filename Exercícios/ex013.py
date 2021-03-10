# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salary = float(input('Enter salary: R$'))
increase = (salary * 1.15)
print(f'The old salary was R${salary} and with the increase it will be worth R${increase:.2f}')
