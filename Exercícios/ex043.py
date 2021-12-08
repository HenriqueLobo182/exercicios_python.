# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# Abaixo de 18,5: ABAIXO DO PESO
# Entre 18,5 e 25: PESO IDEAL
# 25 até 30: SOBREPESO
# 30 até 40: OBESIDADE
# Acima de 40: OBESIDADE MÓRBIDA

weight = float(input('Qual é seu peso em quilogramas? '))  # peso
height = float(input('Qual é sua altura em metros? '))  # altura
imc = (weight / (height ** 2))

if imc < 18.5:
    print('Your body mass index is {:.1f}, portanto, você está ABAIXO DO PESO'.format(imc))

elif 18.5 <= imc < 25:
    print('Your body mass index is {:.1f}, portanto, você está no PESO IDEAL'.format(imc))

elif 25 <= imc < 30:
    print('Your body mass index is {:.1f}, so you have OVERWEIGHT'.format(imc))

elif 30 <= imc < 40:
    print('Your body mass index is {:.1f}, so you have OBESITY'.format(imc))

else:
    print('Your body mass index is {:.1f}, so you have MORBID OBESITY'.format(imc))
