# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado

import mechanize

try:
    biblioteca = mechanize.Browser()
    url = "http://pudim.com.br/"
    biblioteca.open(url)
except:
    print(f'\033[31mNão foi possível acessar o site Pudim \033[m')
else:
    print(f'\033[32mFoi possível acessar o site Pudim \033[m')


print('~'*40)  # OU


import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print('\033[31mDeu erro\033[m')
else:
    print('\033[32mTudo ok\033[m')
    print(site.read())
