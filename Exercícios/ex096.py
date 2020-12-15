# Faça um programa que tenha uma função chamada área(), que recebe as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'A partir dos comprimentos {l}x{c}, temos:')
    print(f'Área correspondente à {a:.1f}m²')


area(l=float(input('Largura [m]: ')),
     c=float(input('Comprimento [m]: ')))
