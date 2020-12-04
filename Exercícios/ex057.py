# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

sexo = str(input('Informe o sexo de uma pessoa: [M/F] ')).upper()[0].strip()

while sexo not in 'FM':
    sexo = str(input('Valor desconhecido. Tente novamente: ')).upper()[0].strip()
print('Sexo {} registrado com sucesso!'.format(sexo))
