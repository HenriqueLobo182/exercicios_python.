# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR')

for c in palavras:
    print(f'\nNa palavra {c} temos: ', end='')
    for vogal in c:
        if vogal in 'AEIOUaeiou':
            print(vogal, end=' ')
