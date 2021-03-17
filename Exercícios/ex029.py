# Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada km acima do limite
# Exemplo: 90 km/h = RS70,00

velocity = float(input('Enter the car speed: [km/h] '))
traffic_ticket_confirmation = velocity > 80.0

if traffic_ticket_confirmation:
    print('You have exceeded the 80km/h limit...')
    traffic_ticket_value = (velocity - 80.0) * 7.0
    print(f'You will have to pay a traffic ticket of R${traffic_ticket_value:.2f}')

else:
    print('You have not exceeded the speed limit.')
