# Crie um programa o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome

name = str(input('Enter your full name: ')).strip()
print(f'Your capitalized name is: {name.upper()}')
print(f'Your name in lower case is: {name.lower()}')

nameWithoutSpaces = name.replace(' ', '')  
print(f'Your full name has {len(nameWithoutSpaces)} letters')
separateName = name.split()
print(f'Your first name has {len(separateName[0])} letters')

print('=-'*20)  # OR

print(f'Your full name has {len(name) - name.count(" ")} letters')
print(f'Your first name has {name.find(" ")} letters')
