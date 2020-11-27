# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o salário: R$'))
aumento = (salario*1.15)
print('O salário antigo era de R${} e o novo vale R${:.2f}'.format(salario, aumento))
