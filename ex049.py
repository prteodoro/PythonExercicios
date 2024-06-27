from time import sleep

exercicio = ' Exercício 049 '
enunciado = """Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que 
agora utilizando um laço for."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(0, 11):
    print(f'{num} x {c} = {num*c}')
    sleep(0.3)
