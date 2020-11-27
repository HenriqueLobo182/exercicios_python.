# Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit

celsius = float(input('Digite a temperatura em °C: '))
fahrenheit = (celsius * 9 / 5) + 32
print('A temperatura {}°C convertido para Fahrenheit passará a valer {}°F'.format(celsius, fahrenheit))
