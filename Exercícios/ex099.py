# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*n):
    print('~'*50)
    print('Analisando os valores informados:')
    cont = mai = 0
    for v in n:
        print(f'{v} ', end='')
        cont += 1
        if cont == 0:
            mai = v
        else:
            if v > mai:
                mai = v

    print(f'Temos o total de {len(n)} números.')
    print(f'E o maior número é {mai}')


maior(2, 6, 10, 3, 6, 1)
maior(3, 8, 4, 5)
maior(7, 4, 3)
maior()
print('~'*50)
