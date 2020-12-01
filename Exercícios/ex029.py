# Faça um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
# foi multado. A multa vai custar R$7,00 por cada km acima do limite
# Exemplo: 90 km/h = RS70,00

v = float(input('Digite a velocidade do carro em km/h: '))
multa = v > 80.0

if multa:
    print('Você ultrapassou o limite de 80 km/h')
    print('Você deverá pagar uma multa de R${:.2f}'.format((v-80.0)*7))
else:
    print('Você não ultrapassou o limite de velocidade')
