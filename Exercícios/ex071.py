# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
# ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Observação: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*35)
print('{:^35}'.format('BANCO PYTHON'))
print('='*35)

v = int(input('Deseja sacar quanto? R$'))  # valor a ser sacado
saldo = v
if v // 50 > 0:
    c50 = v // 50
    print(f'Serão entregues {c50} cédulas de R$50')
    saldo = v % 50

if saldo // 20 > 0:
    c20 = saldo // 20
    print(f'Serão entregues {c20} cédulas de R$20')
    saldo = saldo % 20

if saldo // 10 > 0:
    c10 = saldo // 10
    print(f'Serão entregues {c10} cédulas de R$10')
    saldo = saldo % 10

if saldo // 1 > 0:
    c1 = saldo // 1
    print(f'Serão entregues {c1} cédulas de R$1')
print('='*35)

# OU

valor = int(input('Deseja sacar quanto? R$'))
total = valor
cedula = 50
totalcedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalcedula += 1
    else:
        if totalcedula > 0:
            print(f'Total de {totalcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if total == 0:
            break
