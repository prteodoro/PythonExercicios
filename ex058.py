from random import randint

exercicio = ' Exercício 058 '
enunciado = """Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram 
necessários para vencer."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

print("""Sou seu computador... Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?""")
numpc = randint(0, 10)
palpite = int(input('Qual é seu palpite? '))
qtdpalpites = 1
while palpite != numpc:
    if palpite < numpc:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    qtdpalpites += 1
    palpite = int(input('Qual é seu palpite? '))
print(f'Acertou com {qtdpalpites} tentativa(s). Parabéns!')
