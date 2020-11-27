# Faça um programa que leia a altura e largura de uma parede em metros, calcule a área e a quantidade de tinta
# necessária para pintá-lá, sabendo que cada litro de tinta, pinta uma área de 2m²

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = (altura*largura)
tinta = (area/2)
print('A parede possui dimensão de {}X{} e área de {} m²'.format(largura, altura, area))
print('Serão necessárias {} litros de tinta para pintar a parede'.format(tinta))
