from time import sleep

exercicio = ' Exercício 106 '
enunciado = """Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o 
comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Obs: use cores."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

c = ('\033[m', # 0 sem cores
    '\033[0;30;41m', # 1 vermelho
    '\033[1;1;42m', # 2 verde
    '\033[0;30;43m', # 3 amarelo
    '\033[1;1;44m', # 4 azul
    '\033[0;30;45m', # 5 rosa
    '\033[7;1;40m' # 6 branco
     )


def titulo(msg, cor=0):
    tam = '~' * (len(msg) + 2)
    print(c[cor], end='')
    print(tam)
    print(msg)
    print(tam)
    print(c[0], end='')


def ajuda(com):
    sleep(1.5)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(1.5)


while True:
    titulo('  SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca -> '))
    if comando.strip().upper() == 'FIM':
        break
    else:
        titulo(f"  Acessando o manual do comando '{comando}'", 4)
        ajuda(comando)
titulo('  ATÉ LOGO', 5)
