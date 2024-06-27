exercicio = ' Exercício 073 '
enunciado = """073 - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro 
de Futebol, na ordem de colocação. Depois mostre:
	A) Apenas os 5 primeiros colocados.
	B) Os últimos 4 colocados da tabela.
	C) Uma lista com os times em ordem alfabética.
	D) Em que posição na tabela está o time da Chapecoense."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

tabelabrasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR',
                     'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás',
                     'Bragantino', 'Coritiba', 'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
borda = '=-'*25
print(borda)
print('Lista de times do Brasileirão: ', tabelabrasileirao)
print(borda)
print(f'Os 5 primeiros são {tabelabrasileirao[:5]}')
print(borda)
print(f'Os 4 últimos são {tabelabrasileirao[-4:]}')
print(borda)
print(f'Times em ordem alfabética: {sorted(tabelabrasileirao)}')
print(borda)
print(f'O Santos está na {tabelabrasileirao.index("Santos") + 1}ª posição')
print(borda)
for pos, time in enumerate(tabelabrasileirao):
    if time == 'Palmeiras':
        posicaotime = pos + 1
        timeescolhido = time
print(f'O {timeescolhido} está na {posicaotime}ª posição')

time02 = ''
for cont in range(0, len(tabelabrasileirao)):
    if tabelabrasileirao[cont] == 'Fluminense':
        posicaotime02 = cont + 1
        time02 = tabelabrasileirao[cont]
print(borda)
print('SOLUÇÃO TRÊS')
print(f'O {time02} está na {posicaotime02}ª posição')
