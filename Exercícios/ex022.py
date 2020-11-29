# Crie um programa o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome maiúsculo é {}'.format(nome.upper()))
print('Seu nome minúsculo é {}'.format(nome.lower()))

nse = nome.replace(' ', '')  # nome completo eliminando espaços
print('Seu nome completo possui {} letras'.format(len(nse)))
ns = nome.split()  # separando os nomes
print('Seu primeiro nome possui {} letras'.format(len(ns[0])))

print('==-'*15)  # OU

print('Seu nome completo possui {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))
