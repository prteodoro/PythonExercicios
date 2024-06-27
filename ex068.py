from random import randint

exercicio = ' Exercício 068 '
enunciado = """Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido 
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do 
jogo."""
fim = '-'*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

print('=-'*20)
print(f'VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
vitorias = 0
while True:
    valorjogador = int(input('Diga um valor: '))
    valorpc = randint(0, 10)
    soma = valorjogador + valorpc
    escolhajogador = ' '
    while escolhajogador not in 'PI':
        escolhajogador = str(input(f'Par ou Ímpar? [P/I] ')).strip().upper()[0]
    resultado = ''
    if soma % 2 == 0:
        resultado = 'PAR'
        if escolhajogador == 'P':
            escolhajogador = 'PAR'
    else:
        resultado = 'ÍMPAR'
        if escolhajogador == 'I':
            escolhajogador = 'ÍMPAR'
    print('-' * 40)
    print(f'Você jogou {valorjogador} e o computador {valorpc}. Total de {soma} DEU {resultado}')
    print('-' * 40)
    if escolhajogador == resultado:
        print(f'Você VENCEU!')
        print('Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Você PERDEU!')
        break
    print('=-'*20)
print('=-'*20)
print(f'GAME OVER! Você venceu {vitorias} veze(s).')

