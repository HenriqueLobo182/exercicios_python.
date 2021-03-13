# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

city = str(input('What city were you born in? ')).strip()
nameConfirmation = (city[:5].upper() == 'SANTO')
print(f'{city} begins with the name "Santo"? {nameConfirmation}')
