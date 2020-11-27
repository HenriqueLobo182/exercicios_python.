# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares e quantas libras esterlinas 
#ela pode comprar
# US$1,00 = R$5,39 e £1,00 = R$7,19

r = float(input('Digite quanto você tem na carteira: '))
d = (r/5.39)
l = (r/7.19)
print('Com R${:.2f} você poderá comprar US${:.2f} e £{:.2f}.'. format(r, d, l))
