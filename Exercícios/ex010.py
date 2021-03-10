# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares e quantas libras esterlinas 
#ela pode comprar
# US$1,00 = R$5,39 e £1,00 = R$7,19

reals = float(input('Type how much you have in your wallet: R$'))
dollars = (reals / 5.39)
pounds = (reals / 7.19)
print(f'With R${reals:.2f}, you can buy US${dollars:.2f} and £{pounds:.2f}')
