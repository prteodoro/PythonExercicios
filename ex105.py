exercicio = ' Exercício 105 '
enunciado = """Faça um programa que tenha uma função notas() que pode receber várias notas 
de alunos e vai retornar um dicionário com as seguintes informações:
	- Quantidade de notas
	- A maior nota
	- A menor nota
	- A média da turma
	- A situação (opcional)
Adicione também as docstrings da função."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n) / turma['total']
    if sit:
        if turma['média'] < 5:
            turma['situação'] = 'RUIM'
        elif turma['média'] < 7:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'BOA'
    return turma


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
