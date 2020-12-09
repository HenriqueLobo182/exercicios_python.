# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

lista = list()
for c in range(0, 5):
    n = int(input('Digite um número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'{n} adicionado na última posição')
    else:
        for pos in range(0, 4):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'{n} adicionado na posição {pos}')
                break
    print('~'*30)
print(f'A lista ordenada corresponde a: {lista}')
