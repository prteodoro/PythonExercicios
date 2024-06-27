exercicio = ' Exercício 042 '
enunciado = """Reforça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de 
triângulo será formado:
	- Equilátero: todos os lados iguais
	- Isósceles: dois lados iguais
	- Escaleno: todos os lados diferentes"""
fim = '=' * 30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

reta01 = float(input('Primeiro segmento: '))
reta02 = float(input('Segundo segmento: '))
reta03 = float(input('Terceiro segmento: '))
if reta01 >= reta02 + reta03 or reta02 >= reta01 + reta03 or reta03 >= reta01 + reta02:
    print(f'Os segmentos acima NÃO PODEM formar triângulo!')
elif reta01 == reta02 and reta01 == reta03:
    print(f'Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
elif reta01 != reta02 and reta01 != reta03 and reta02 != reta03:
    print(f'Os segmentos acima PODEM FORMAR um triângulo ESCALENO!')
else:
    print(f'Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
