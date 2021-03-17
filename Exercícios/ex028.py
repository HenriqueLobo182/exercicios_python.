# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('==-'*12)
print('I will think of a number from 0 to 5')
print('==-'*12)
sleep(1)

computerNumber = randint(0, 5)  
userNumber = int(input('What number I thought? '))  
print('PROCESSING...')
sleep(1)

if computerNumber == userNumber:
    print('Congratulations you guessed the number!')
else:
    print(f'I chose number {computerNumber} and not number {userNumber}. Try again!')
