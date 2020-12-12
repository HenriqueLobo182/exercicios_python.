# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em lista. No final, mostre:
# Quantas pessoas foram cadastradas
# Uma listagem com as pessoas mais pesadas. pessoas com peso maior
# Uma listagem com as pessoas mais leves.

pessoas = list()
dados = list()
pesado = list()
leve = list()
qnt = maior_peso = menor_peso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if qnt == 0:
        maior_peso = menor_peso = dados[1]
        pesado.append(dados[0])
        leve.append(dados[0])
    else:
        if dados[1] == maior_peso:  # se valor do peso igual, recebe nome da pessoa
            pesado.append(dados[0])

        if dados[1] == menor_peso:  # se valor do peso igual, recebe nome da pessoa
            leve.append(dados[0])

        elif dados[1] > maior_peso:  # se valor do peso maior, recebe novo peso e novo nome, perdendo o nome anterior
            maior_peso = dados[1]
            pesado.clear()
            pesado.append(dados[0])

        elif dados[1] < menor_peso:  # se valor do peso menor, recebe novo peso e novo nome, perdendo o nome anterior
            menor_peso = dados[1]
            leve.clear()
            leve.append(dados[0])
    qnt += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if 'N' in continuar:
        break
    pessoas.append(dados[:])
    dados.clear()
print(f'Foram cadastradas {qnt} pessoas')
print(f'Com {maior_peso}kg, {pesado} possuem o maior peso')
print(f'Com {menor_peso}kg, {leve} possuem o menor peso')


print('~'*50)  # OU


temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar [S/N]? '))[0]
    if resp in 'Nn':
        break
print('=-'*20)
print(f'Ao todo foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi {mai}kg, peso de: ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {men}kg, peso de: ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}] ', end='')
