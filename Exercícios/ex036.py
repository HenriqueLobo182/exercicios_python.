# Escreva um programa para aprovar o empréstimo bancário de uma casa. O programa vai perguntar o valor da casa, o
# salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

color = {'vermelho': '\033[31m', 'verde': '\033[32m', 'limpa': '\033[m'}

vc = float(input('Valor da casa: R$'))  # valor da casa
sf = float(input('Salário do comprador: R$'))  # salário do funcionário
ae = int(input('Anos de pagamento: '))  # anos do empréstimos

pm = vc / (ae*12)

if pm <= (sf*0.3):
    print('{}Empréstimo aceito!{} O valor mensal da prestação será de R${:.2f}'.format(color['verde'], color['limpa'], pm))
else:
    print('{}Empréstimo negado! A prestação de R${:.2f} excede 30% do salário do funcionário'.format(color['vermelho'], pm))
