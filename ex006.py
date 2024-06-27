exercicio = " Exercício 006 "
enunciado = 'Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2) #pow(n, (1/2))

#print(f'Analisando o valor {n}, seu dobro é {n*2}, seu triplo é {n*3} e a sua raiz quadrada é {n**(1/2}.')
print(f'Analisando o valor {n}, seu dobro é {dobro}, seu triplo é {triplo} e a sua raiz quadrada é {raiz:.2f}.')
