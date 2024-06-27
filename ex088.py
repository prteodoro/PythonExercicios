from random import randint
from time import sleep

exercicio = ' Exercício 088 '
enunciado = """Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa 
vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

print(f'{"JOGAR NA MEGA SENA":^40}')
print('-'*40)
qtdejogos = int(input('Quantos jogos você quer que eu sorteie? '))
aposta = []
totalapostas = []
print('-=' * 3, f'SORTEANDO {qtdejogos} JOGOS', '-=' * 3)
sleep(1)
for c in range(0, qtdejogos):
    for pos in range(0, 6):
        numsorteado = randint(1, 60)
        while True:
            if numsorteado not in aposta:
                aposta.append(numsorteado)
                break
            else:
                numsorteado = randint(1, 61)
    aposta.sort()
    totalapostas.append(aposta[:])
    aposta.clear()
for pos, jogo in enumerate(totalapostas):
    print(f'Jogo {pos + 1}: {jogo}')
    sleep(1)
print('-=' * 5, f'BOA SORTE', '-=' * 5)
