# Melhore o DESAFIO 061, perguntando se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que
# quer mostrar 0 termos.

print('=-'*15)
print("""Progressão aritmética""")
print('=-'*15)

termo = int(input('Informe o termo: '))
razao = int(input('Razão: '))
soma = termo
c = 1
termos = 1
maistermos = 1

while c < 10:
    if c == 1:
        print(termo, end=' -> ')
        soma += razao
    else:
        soma += razao
    c += 1
    print(soma, end=' -> ')
    if c == 10:
        print('FIM')

    while c > 9 and maistermos != 0:
        maistermos = int(input("""Deseja mostrar mais quantos termos? """))
        if maistermos == 0:
            break
        else:
            for cont in range(0, maistermos):
                soma += razao
                print(soma, end=' -> ')
                termos += 1
            print('FIM')
    termos += 1
print('FIM')
print('Foram mostrados {} termos da PA'.format(termos))

print('=-'*40)  # OU

primeiro2 = int(input('Digite o termo: '))
razao2 = int(input('Razão: '))
termo2 = primeiro2
cont2 = 1
total2 = 0
mais2 = 10
while mais2 != 0:
    total2 += mais2
    while cont2 <= total2:
        print('{} -> '.format(termo2), end='')
        termo2 += razao2
        cont2 += 1
    print('PAUSA')
    mais2 = int(input('Quantos termos você quer ver mais? '))
print('FIM')
print('Progressão com {} termos mostrados'.format(total2))
