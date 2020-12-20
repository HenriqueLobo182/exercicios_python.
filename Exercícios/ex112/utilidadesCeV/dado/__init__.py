def LeiaDinheiro(txt):
    while True:
        res = str(input(txt)).replace(',', '.').strip()
        if res.isalpha() or res == '':
            print(f'\033[31mERRO! "{res}" é um valor inválido\033[m')
        else:
            txt = float(res)
            break
    return txt
