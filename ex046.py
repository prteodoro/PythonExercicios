from time import sleep

exercicio = ' Exercício 046 '
enunciado = """Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de 
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

for contador in range(10, -1, -1):
    print(contador)
    sleep(0.5)
print(f'BUM! BUM! POOOW!')

