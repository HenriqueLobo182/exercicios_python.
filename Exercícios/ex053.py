# Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.
# Exemplo: apos a sopa

cores = {'ciano': '\033[1:36m', 'vermelho': '\033[31m', 'amarelo': '\033[33m', 'limpa': '\033[m'}

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')  # frase formatada maiúscula.
fi = frase[::-1]  # frase invertida.

if frase == fi:
    print('{}{}{} tem como frase inversa {}{}{}, \nportanto, formam um PALÍNDROMO'.format(cores['ciano'], frase,
                                                                                          cores['limpa'], cores['ciano'],
                                                                                          fi, cores['limpa']))
else:
    print('{}{}{} tem como frase inversa {}{}{}, \nlogo, não formam um PALÍNDROMO'.format(cores['vermelho'], frase,
                                                                                          cores['limpa'],
                                                                                          cores['vermelho'], fi,
                                                                                          cores['limpa']))

print('=-'*20)

f1 = str(input('Digite uma frase: ')).strip().upper()
palavras = f1.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('{}{}{} e {}{}{}'.format(cores['amarelo'], junto, cores['limpa'], cores['amarelo'], inverso, cores['limpa']))
if inverso == junto:
    print('PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')
