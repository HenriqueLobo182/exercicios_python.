# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número enter 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Tente adivinhar o número entre 0 e 10 escolhido pelo computador: ')
ec = randint(0, 10)  # escolha do computador
eu = 0  # escolha do usuário
tentativas = 0
while eu != ec:
    eu = int(input('Digite um número: '))
    tentativas += 1
    if eu != ec:
        if eu < ec:
            print('Tente novamente! O computador escolheu um valor maior!')
        else:
            print('Tente novamente! O computador escolheu um número menor!')
print('Parabéns! Após {} tentativas você adivinhou!'.format(tentativas))

print('=-'*30)  # OU

computador = randint(0, 10)
print('Pensei em um número de 0 a 10.')
print('Qual número pensei?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
print('ACERTOU com {} tentativas'.format(palpites))
