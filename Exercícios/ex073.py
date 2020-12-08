# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:
# Apenas os 5 primeiros colocados.
# Os últimos colocados da tabela.
# Uma lista com os times em ordem alfabética
# Em que posição na tabela está o time da Chapecoense. Chapecoense em 2020 está na série B, usei como exemplo o Bragantino.

tabela = ('São Paulo', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Fluminense', 'Palmeiras', 'Santos', 'Internacional',
          'Ceará', 'Fortaleza', 'Corinthians', 'Athletico-PR', 'Bahia', 'Bragantino', 'Atlético-GO', 'Sport', 'Vasco',
          'Coritiba', 'Botafogo', 'Goiás')

print('~'*30)
print(f'20 times da série A {tabela}')
print('~'*30)
print(f'5 primeiros colocados são {tabela[:5]}')
print('~'*30)
print(f'Últimos colocados são {tabela[-4:]}')
print('~'*30)
print(f'Times por ordem alfabética {sorted(tabela)}')
print('~'*30)
print(f'Bragantino está em {tabela.index("Bragantino")+1}º lugar')
