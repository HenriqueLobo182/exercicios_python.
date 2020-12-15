# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.

def escreva(txt):
    centro = len(txt) + 6
    print(f'~~~{"~"*len(txt)}~~~')
    print(f'{txt:^{centro}}')
    print(f'~~~{"~"*len(txt)}~~~')


escreva(str(input('Escreva um frase: ')))
