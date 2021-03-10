# Escreva um programa que converta uma temperatura digitada em graus Celsius e converta para graus Fahrenheit

celsius = float(input('Digite a temperatura em °C: '))
fahrenheit = (celsius * 9 / 5) + 32
print(f'The temperature {celsius}°C converted to Fahrenheit will be worth {fahrenheit:.1f}°F')
