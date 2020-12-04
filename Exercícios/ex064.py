# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

s = c = n = 0  # soma, contador e número digitado pelo usuário

while n != 999:
    print('Se quiser parar digite 999!')
    n = int(input('Digite um número: '))
    print('~'*30)
    if n != 999:
        s += n
        c += 1
print('A soma entre todos os {} valores digitados vale {}'.format(c, s))

print('=-'*20)  # OU

cont = soma = 0
num = int(input('Digite um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} valores e soma entre eles vale {}'.format(cont, soma))
