# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag)

s = c = 0  # soma e contagem
while True:
    n = int(input('Digite um valor [999 para interromper]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitados {c} valores e soma entre eles vale {s}.')
