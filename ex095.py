from time import sleep

exercicio = ' Exercício 095 '
enunciado = """Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um 
sistema de visualização de detalhes do aproveitamento de cada jogador."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

jogador = {}
golspartidas = []
equipe = []
resposta = ''
while resposta != 'N':
    jogador['Nome'] = str(input('Nome do jogador: ')).strip().capitalize()
    totalpartidas = int(input(f'Qunatas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, totalpartidas):
        golspartidas.append(int(input(f'   Quantos gols na partida {c+1}? ')))
    jogador['gols'] = (golspartidas.copy())
    jogador['total'] = sum(golspartidas)
    golspartidas.clear()
    equipe.append(jogador.copy())
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*30)
print(equipe)
print(f'{"cod":<3} {"nome":<13} {"gols":<13} {"total":<5}')
print('-'*36)
for p, v in enumerate(equipe):
    print(f'{str(p+1):>3} ', end='')
    for j in v.values():
        print(f'{str(j):<13} ', end='')
    sleep(1)
    print()
print('-'*36)
while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if cod == 999:
        break
    cod = cod - 1
    if cod >= len(equipe) or cod < 0:
        print(f'ERRO! Não existe jogador com o código {cod+1}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {equipe[cod]["Nome"]}:')
        for jogo, gols in enumerate(equipe[cod]["gols"]):
            print(f'   No jogo {jogo+1} fez {gols} gols.')
            sleep(1)
    print('-'*32)
print('-'*32)
print(f'<< PROGRAMA ENCERRADO >>')
