exercicio = ' Exercício 035 '
enunciado = """Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem 
ou não formar um triângulo."""
fim = '='*30
print(f'{exercicio:=^30} \n {enunciado} \n{fim}')

print('-=-' * 17)
print(f'Analisador de Triângulos')
print('-=-' * 17)
reta01 = float(input('Primeiro segmento: '))
reta02 = float(input('Segundo segmento: '))
reta03 = float(input('Terceiro segmento: '))
if reta01 < reta02 + reta03 and reta02 < reta01 + reta03 and reta03 < reta01 + reta02:
    print(f'Os segmentos acima PODEM FORMAR triângulo!')
else:
    print(f'Os segmentos acima NÃO PODEM formar triângulo!')
