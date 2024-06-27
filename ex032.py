from datetime import date

exercicio = ' Exercício 032 '
enunciado = 'Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

ano = int(input('Qual ano deseja saber se é BISSEXTO? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 100 == 0 and ano % 400 != 0 or ano % 4 != 0:
    print(f'O ano {ano} NÃO é BISSEXTO.')
else:
    print(f'O ano {ano} é BISSEXTO.')





