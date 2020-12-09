# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista = list()
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Número salvo com sucesso')
    else:
        print('Número repetido, tente outro.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if continuar in 'N':
        break
    print('~'*30)
lista.sort()
print(f'Você digitou: {lista}')
