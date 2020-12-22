# Crie um pequeno sistema modular que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter duas opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from ex115.funções import ação

ação('\033[1;33m[0]\033[m - \033[34mVer pessoas cadastradas\n\033[m'
            '\033[1;33m[1]\033[m - \033[34mCadastrar novas pessoas\n\033[m'
            '\033[1;33m[2]\033[m - \033[34mSair do programa \n\033[m'
            'Sua opção: ')
