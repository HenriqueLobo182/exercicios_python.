# Crie um pacote chamado utilidades CeV que tenhas dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

from ex111.utilidadesCeV import moeda

p = float(input('Digite um valor: R$'))
moeda.resumo(p, 35, 22)
