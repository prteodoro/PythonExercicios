exercicio = ' Exercício 093 '
enunciado = """Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa 
vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos 
em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols 
feitos durante o campeonato."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

jogador = {}
golspartida = []
jogador['nome'] = str(input('Nome do Jogador: '))
totalpartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, totalpartidas):
    golspartida.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = golspartida
jogador['total'] = sum(golspartida)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {totalpartidas} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f'  => Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')


