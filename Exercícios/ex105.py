# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com
# as seguinte informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione também as docstrings da função.

nota = {}


def notas(*n, sit=False):
    """
    -> Analisa a situação após a análise de notas de vários alunos
    :param n: notas dos alunos
    :param sit: (valor opcional) mostra ou não a situação
    :return: retorna um dicionário
    """

    nota['total'] = len(n)
    nota['maior'] = max(n)
    nota['menor'] = min(n)
    nota['média'] = sum(n)/len(n)

    if sit:
        if nota['média'] >= 7:
            nota['situação'] = 'BOA'
        elif nota['média'] < 6:
            nota['situação'] = 'RUIM'
        else:
            nota['situação'] = 'RAZOÁVEL'

    return nota


resp = notas(5.5, 6.5, 8.5, sit=True)
print(resp)
help(notas)
