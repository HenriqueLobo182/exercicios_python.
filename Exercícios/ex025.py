# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

name = str(input('Enter your full name: ')).strip()
nameConfirmation = ('SILVA' in name.upper())
print(f'{name} has the name "Silva"? {nameConfirmation}')
