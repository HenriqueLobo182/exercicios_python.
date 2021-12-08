# Escreva um programa que leia um número Inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário.
# 2 para octal.
# 3 para hexadecimal.

number = int(input('Type a number: '))

print('==-'*15)
print('[1] for binaty.')
print('[2] for octal')
print('[3] for hexadecimal')
userChoice = int(input('Choose conversion: '))  

if userChoice == 1:
    print(f'The number {number} in binary corresponds to {bin(number)[2:]}')
elif userChoice == 2:
    print(f'The number {number} in octal corresponds to {oct(number)[2:]}')
elif userChoice == 3:
    print(f'The number {number} in hexadecimal corresponds to {hex(number)[2:]}')
else:
    print('Choose a valid conversion!')
