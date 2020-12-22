from time import sleep


def título(txt):
    print('~'*50)
    print(f'{txt:^50}')
    print('~'*50)


def ação(a=0):
    while True:
        título('CADASTRO DE PESSOAS')
        try:
            comando = int(input(a))
        except:
            print('\033[31mPor favor! Digite um comando válido\033[m')
            continue

        else:
            if comando == 0:
                título('PESSOAS CADASTRADAS')
                try:
                    abrir = open('pessoas.txt', 'r+')
                    print(abrir.read())
                    abrir.close()

                except FileNotFoundError:
                    abrir = open('pessoas.txt', 'w+')
                abrir.close()

            elif comando == 1:
                título('Opção 1')
                try:
                    n = nome('Digite seu nome: ')
                    i = idade('Digite sua idade: ')
                    acrescentar = open('pessoas.txt', 'a')

                except FileNotFoundError:
                    abrir = open('pessoas.txt', 'w+')

                else:
                    acrescentar.write(f'{n:<40} {i:>4} anos')
                    acrescentar.write('\n')
                    acrescentar.close()

            elif comando == 2:
                título('Saindo do sistema')
                sleep(1)
                break

            else:
                print('\033[31mPor favor! Digite um comando válido\033[m')
        sleep(1)


def nome(n=''):
    while True:
        try:
            txt = str(input(n))
        except:
            print('Digite um valor correto')
            continue
        else:
            return txt


def idade(i=0):
    while True:
        try:
            idad = int(input(i))
        except:
            print('Informe um valor correto')
            continue
        else:
            return idad
