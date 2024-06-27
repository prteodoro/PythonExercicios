from random import randint
from time import sleep

exercicio = ' Exercício 100 '
enunciado = """Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e somapar(). A primeira função vai sortear 5 números e vai colocá-los dentro da 
lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela 
função anterior."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

numeros = []


def sorteia(lista):
    lista.clear()
    print(f'Sorteando 5 valores da lista: ', end='')
    sleep(0.5)
    for v in range(0, 5):
        num = randint(1, 10)
        print(f'{num} ', end='')
        lista.append(num)
        sleep(0.4)
    print(f'PRONTO!')


def somapar(lista):
    totalpar = 0
    for p in numeros:
        if p % 2 == 0:
            totalpar += p
    print(f'Somando os valores pares de {numeros}, temos {totalpar}')


sorteia(numeros)
somapar(numeros)
sorteia(numeros)
somapar(numeros)
