# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em posição ela aparece a última vez

phrase = str(input('Type a phrase: ')).strip().upper()
number_of_letters_a = phrase.count('A')
first_a = (phrase.find('A') + 1)
last_a = (phrase.rfind('A') + 1)
print(f'The letter "A" appears {number_of_letters_a} times')
print(f'The first letter "A" appears in the {first_a}º position')
print(f'The last letter "A" appears in the {last_a}º position')
