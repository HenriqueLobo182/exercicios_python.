# Crie um programa que leia nome, ano de nascimento e de carteira de trabalho e cadastre-os (com idade) em um dicionário
# se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além de idade, com quantos anos a pessoa vai se aposentar.
# 35 anos de contribuição

from datetime import date

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input('Carteira de trabalho: (0 se não tiver) '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano do primeiro emprego: '))
    pessoa['salário'] = float(input('Salário primeiro emprego: R$'))
    pessoa['aposentadoria'] = pessoa['contratação'] + 35 - nascimento
print('~'*40)
for k, v in pessoa.items():
    print(f' - {k} é igual a {v}')
