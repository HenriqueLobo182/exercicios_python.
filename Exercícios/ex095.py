# Aprimore o desafio 093 para que ele funcione cmo vários jogadores, incluindo um sistema de visualização de detalhes de
# aproveitamento de cada jogador.

jogadorlista = list()

while True:
    jogador = dict()
    golslista = list()
    totalgols = 0

    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'{jogador["nome"]} disputou quantas partidas? '))

    for c in range(0, partidas):
        gols = int(input(f'Gols de {jogador["nome"]} na {c+1}ª partida: '))
        golslista.append(gols)
        totalgols += gols

    jogador['gols'] = golslista
    jogador['total'] = totalgols
    jogadorlista.append(jogador.copy())

    continuar = ' '
    while continuar not in 'NS':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if 'N' in continuar:
        break
    print('~'*40)

print('~'*60)
print('Cod | Nome      | Gols                     | Total')
for i, v in enumerate(jogadorlista):
    print(f'{i:<4}|{jogadorlista[i]["nome"]:<10} | {str(jogadorlista[i]["gols"]):<15} {"|":>10} {jogadorlista[i]["total"]}')
print('~'*60)

while True:
    escolha = int(input(f'Deseja ver qual jogador? [0/ {len(jogadorlista) - 1}] [999 para parar] '))
    if escolha >= len(jogadorlista) or escolha < 0:
        print(f'Valor {escolha} não existe')
    elif escolha == 999:
        break
    else:
        print(f'{jogadorlista[escolha]["nome"]} jogou {len(jogadorlista[escolha]["gols"])} partidas')
        for c, g in enumerate(jogadorlista[escolha]["gols"]):
            print(f' => Na partida {c+1}, fez {g} gols')
        print(f'Ao todo fez {jogadorlista[escolha]["total"]} gols')
    print('~'*50)
