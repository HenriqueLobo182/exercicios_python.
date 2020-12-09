# Crie um programa onde o usuário digite uma espressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
# expressão passada está com os parênteses abertos e fechados na ordem correta.

e = str(input('Digite uma expressão matemática: '))
aberto = e.count('(')
fechado = e.count(')')
if aberto != fechado:
    print('Expressão matemática incorreta')
else:
    print('Expressão matemática correta')

print('=-'*20)

exp = str(input('Digite a expressão: '))
pilha = []
for simbolo in exp:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada')
