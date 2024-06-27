from time import sleep

exercicio = ' Exercício 098 '
enunciado = """Faça um programa que tenha uma função chamada contador(), que receba três 
parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
	A) De 1 até 10, de 1 em 1
	B) De 10 até 0, de 2 em 2
	C) Uma contagem personalizada."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')


def contagem(inicio, fim, passo):
    print('-='*15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.5)
    if passo < 0:
        passo *= -1
    if inicio > fim:
        passo *= -1
        fim -= 2
    for v in range(inicio, fim+1, passo):
        sleep(0.3)
        print(f'{v} >> ', end='')
    print(f'FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
while True:
    print('-='*15)
    print(f'Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    contagem(i, f, p)
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-'*50)
print(f'<< PROGRAMA ENCERRADO >>')
