# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a
# tabela abaixo:
# Abaixo de 18,5: ABAIXO DO PESO
# Entre 18,5 e 25: PESO IDEAL
# 25 até 30: SOBREPESO
# 30 até 40: OBESIDADE
# Acima de 40: OBESIDADE MÓRBIDA

p = float(input('Qual é seu peso em quilogramas? '))  # peso
a = float(input('Qual é sua altura em metros? '))  # altura
imc = (p / (a ** 2))

if imc < 18.5:
    print('Seu índice é de  {:.1f}, portanto, você está ABAIXO DO PESO'.format(imc))

elif 18.5 <= imc < 25:
    print('Seu índice é de {:.1f}, portanto, você está no PESO IDEAL'.format(imc))

elif 25 <= imc < 30:
    print('Seu índice é de {:.1f}, portanto, você está com SOBREPESO'.format(imc))

elif 30 <= imc < 40:
    print('Seu índice é de {:.1f}, portanto, você está com OBESIDADE'.format(imc))

else:
    print('Seu índice é de {:.1f}, portanto, você está com OBESIDADE MÓRBIDA'.format(imc))
