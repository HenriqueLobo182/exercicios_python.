# Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro e o último nome separadamente
# Exemplo: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

name = str(input('Enter your full name: ')).strip()
splitName = name.split()
firstName = splitName[0]
lastName = splitName[-1]
print(f'Your first name is {firstName}')
print(f'Your last name is {lastName}')
