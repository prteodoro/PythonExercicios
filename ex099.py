from time import sleep

exercício = ' Exercício 099 '
enunciado = """Faça um programa que tenha uma função chamada maior(), que receba vários 
parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior."""
fim = '='*50
print(f'{exercício:=^50} \n{enunciado} \n{fim}')


def maior(* valores):
    print('-='*30)
    sleep(1)
    print(f'Analisando os valores passados...')
    sleep(1)
    cont = maiorvalor = 0
    for v in valores:
        if cont == 0:
            maiorvalor = v
        if v > maiorvalor:
            maiorvalor = v
        print(f'{v} ', end='')
        sleep(0.3)
        cont += 1
    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maiorvalor}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
