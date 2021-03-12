# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kilometers = float(input('How many kilometers were traveled with the vehicle? '))
days = int(input('For how many days the car has been rented? '))
total = (kilometers * 0.15) + (days * 60)
print(f'The total to be paid will be R${total:.2f}')
