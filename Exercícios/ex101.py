# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições

def voto(n):
    from datetime import date
    idade = date.today().year - n
    if idade < 16:
        return f"Você possui {idade} anos, portanto, VOTO NEGADO"
    elif 18 <= idade <= 65:
        return f"Você possui {idade} anos, portanto, VOTO OBRIGATÓRIO"
    else:
        return f"Você possui {idade} anos, portanto, VOTO OPCIONAL"


nasc = int(input('Ano de nascimento: '))
print(f'{voto(nasc)}')
