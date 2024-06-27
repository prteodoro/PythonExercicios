from time import sleep

exercício = ' Exercício 051 '
enunciado = """Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
mostre os 10 primeiros termos dessa progressão."""
fim = '='*30
print(f'{exercício:=^30} \n{enunciado} \n{fim}')

print(f'{" 10 TERMOS DE UMA PA ":=^30}')
primeirotermo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termos = primeirotermo
for c in range(0, 10):
    print(termos, end=' → ')
    termos += razao
    sleep(0.3)
print('ACABOU')
