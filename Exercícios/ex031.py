# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km e R$0,45 para viagens mais longas

d = float(input('Digite a distância da viagem em km: '))  # distância da viagem
pn = (d <= 200)  # preço normal da viagem
if pn:
    print('O valor da viagem será de R${:.2f}'.format(d*0.5))
else:
    print('O valor da viagem será de R${:.2f}'.format(d*0.45))

print('=-'*20)  # OU

preco = d * 0.50 if d <= 200 else d * 0.45
print('O valor da viagem será de R${:.2f}'.format(preco))
