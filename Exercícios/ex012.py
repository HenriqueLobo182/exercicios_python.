# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Digite o preço do produto: R$'))
desconto = (preço*0.95)
print('Com o desconto de 5%, o produto passará a valer R${:.2f}'.format(desconto))
