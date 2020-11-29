# Faça um programa que leia o nome completo de uma pessoa, mostrando o primeiro e o último nome separadamente
# Exemplo: Ana Maria de Souza
# Primeiro: Ana
# Último: Souza

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu primeiro nome é {}'.format(nome.split()[0]))
print('Seu último nome é {}'.format(nome[nome.rfind(' ')+1:]))

print('==-'*15)  # OU

n = nome.split()
print('Seu último nome é {}'.format(n[len(n)-1]))
