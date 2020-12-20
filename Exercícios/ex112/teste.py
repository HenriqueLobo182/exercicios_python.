# Dentro do pacote utilidade CeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcioanar como a função input(), mas com umas validação da dados para aceitar apenas
# valores que sejam monetários.

from ex112.utilidadesCeV import dado, moeda

p = dado.LeiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 35)
