exercicio = ' Exercício 081 '
enunciado = """Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
	A) Qunatos números foram digitados.
	B) A lista de valores, ordenada de forma decrescente.
	C) Se o valor 5 foi digitado e está ou não na lista."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resposta = str(input('Quer coninuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Quer coninuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('-='*25)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista.')
