# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# utilizando WHILE.

print('=-'*20)
print('10 primeiros termos de uma PA')
print('=-'*20)

termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
soma = termo
c = 1
while c <= 10:
    if c == 1:
        print(soma, end=' -> ')
    soma += razao
    c += 1
    print(soma, end=' -> ')
print('FIM')
