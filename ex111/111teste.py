from utilidadesCeV import moeda

exercicio = ' Exercício 111 '
enunciado = """Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados cadastro e dado.
Transfira todas as funções utilizadas nos desafios 107, 108, 109 e 110 para o primeiro pacote e mantenha 
tudo funcionando."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valor = float(input('Digite o preço: R$'))
moeda.resumo(valor, 20, 12)

