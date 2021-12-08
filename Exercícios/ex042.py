# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero : todos lados iguais.
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.

side01 = float(input('Fisrt side: '))
side02 = float(input('Second side: ')) 
side03 = float(input('Third side: ')) 

condition_for_triangle_existence = ((side01 + side02) > side03 and (side01 + side03) > side02 and (side02 + side03) > side01)
equilatero_existence = (side01 == side02 == side03)
isosceles_existence = (side01 == side02 or side01 == side03 or side02 == side03)
escaleno_existence = (side01 != side02 != side03 != side01)

if condition_for_triangle_existence and equilatero_existence:
    print(f'The sides {side01}, {side02} e {side03} can form an equilateral triangle')

elif condition_for_triangle_existence and isosceles_existence:
    print(f'The sides {side01}, {side02} e {side03} can form an isosceles triangle')

elif condition_for_triangle_existence and escaleno_existence:
    print(f'The sides {side01}, {side02} e {side03} can form an scalene triangle')

else:
    print(f'The sides {side01}, {side02} e {side03} can not form an triangle')
