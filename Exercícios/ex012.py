# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

price = float(input('Enter product price: R$'))
discount = (price * 0.95)
print(f'With the 5% discount, the product will be worth R${discount:.2f}')
