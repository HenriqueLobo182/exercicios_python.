# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

phrase = input('Type something: ')
print(f"'{phrase}' has as its primitive type {type(phrase)}")
print(f"'{phrase}' has only spaces? {phrase.isspace()}")
print(f"'{phrase}' it's a number? {phrase.isnumeric()}")
print(f"'{phrase}' it's alphabetic? {phrase.isalpha()}")
print(f"'{phrase}' it's alphanumeric? {phrase.isalnum()}")
print(f"'{phrase}' it's all in capital letters? {phrase.isupper()}")
print(f"'{phrase}' it's all in lowercase letters? {phrase.islower()}")
print(f"'{phrase}' it's all capitalized? {phrase.istitle()}")
