# Crie um programa que gerencie um aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# adicionado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = dict()
golslista = list()

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'{jogador["nome"]} disputou quantas partidas? '))

totalgols = 0
for c in range(0, partidas):
    gols = int(input(f'Gols na {c+1}ª partida: '))
    golslista.append(gols)
    totalgols += gols

print('~'*40)
jogador['gols'] = golslista
jogador['total'] = totalgols
print(jogador)
print('~'*40)
for k, v in jogador.items():
    print(f'{k} recebe {v}')

print('~'*40)
print(f'{jogador["nome"]} jogou {partidas} partidas')
for i, v in enumerate(golslista):
    print(f' => Na partida {i+1}, fez {v} gols')
print(f'Ao todo fez {totalgols} gols')
