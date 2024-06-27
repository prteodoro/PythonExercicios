exercicio = ' Exercício 103 '
enunciado = """Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros 
opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido 
informado corretamente."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')


def ficha(nome='<desconhecido>', gols=0):
    return print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: ')).strip().capitalize()
g = str(input('Número de Gols: ')).strip()
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)

