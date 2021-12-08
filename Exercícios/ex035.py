# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

side01 = float(input('First side: '))
side02 = float(input('Second side: '))
side03 = float(input('Third side: '))

condition_to_be_a_triangle = (side01 + side02) > side03 and (side02 + side03) > side01 and (side03 + side01) > side02
t = ((side01+side02) > side03 and (side02+side03) > side01 and (side03+side01) > side02)  

if condition_to_be_a_triangle:
    print(f'Sides {side01}, {side02} and {side03} can form a tringle')
else:
    print(f'Sides {side01}, {side02} and {side03} cannot form a tringle')
