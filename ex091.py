from random import randint
from time import sleep
from operator import itemgetter

exercicio = ' Exercício 091 '
enunciado = """Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em ordem, sabendo que o vencedor tirou o maior número 
no dado."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = []
print(f'Valores sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-='*20)
print(f'  == RANKING DOS JOGADORES ==')
for p, v in enumerate(ranking):
    print(f'{p+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)

