# Faça um programa que leia a altura e largura de uma parede em metros, calcule a área e a quantidade de tinta
# necessária para pintá-lá, sabendo que cada litro de tinta, pinta uma área de 2m²

height = float(input('How tall is the wall? [meters] '))
width = float(input('How wide is the wall? [meters] '))
area = (height * width)
paint = (area / 2)
print(f'The wall has a dimension of {height}x{width} and an area of {area} m²')
print(f'{paint:.2f} liters of paint will be needed to paint the wall')
