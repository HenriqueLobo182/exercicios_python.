# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento.
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Valor do produto: R$'))  # preço normal do produto
print('==-'*15)
print(""" [1] para à vista dinheiro/cheque
 [2] para à vista no cartão
 [3] para até 2x no cartão
 [4] para 3x ou mais no cartão""")
fp = int(input('Qual a forma de pagamento: '))  # forma de pagamento

if fp == 1:
    nv = (valor * 0.90)  # novo valor
    print("""Escolhendo o pagamento à vista dinheiro/cheque, 
o produto passará a valer R${:.2f} com desconto""".format(nv))

elif fp == 2:
    nv = (valor * 0.95)
    print("""Escolhendo o pagamento à vista no cartão, 
o produto passará a valer R${:.2f} com desconto""".format(nv))

elif fp == 3:
    vp = (valor / 2)  # valor das parcelas
    print("""Escolhendo o pagamento até 2x no cartão, 
o produto vale R${:.2f} sem juros
e sua parcela será de R${:.2f}""".format(valor, vp))

elif fp == 4:
    nv = (valor * 1.20)  # novo valor com juros escolhendo 3x ou mais no cartão
    p = int(input('Quantas parcelas? '))  # escolha de parcelas pelo usuário
    vp = nv / p  # valor das parcelas
    print("""Escolhendo o pagamento {}x no cartão, 
o produto passará a valer R${:.2f} no final com juros,
parcelados em R${:.2f}""".format(p, nv, vp))

else:
    print('Informe uma forma de pagamento válida!')
