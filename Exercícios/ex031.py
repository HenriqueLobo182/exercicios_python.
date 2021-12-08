# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas

distance = float(input('Enter travel distance: [km] ')) 
if distance <= 200:
    tripPrice = distance * 0.50 
    print(f'The value of the trip will be R${tripPrice:.2f}')
else:
    tripPrice = distance * 0.45
    print(f'The value of the trip will be R${tripPrice:.2f}')

print('=-'*20)  # OR

price = distance * 0.50 if distance <= 200 else distance * 0.45
print(f'The value of the trip will be R${price:.2f}')