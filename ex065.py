exercicio = ' Exercício 065 '
enunciado = """Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valor lido. O programa deve 
perguntar ao usuário se ele quer ou não continuar a digitar valores."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')
resposta = 'S'
contador = soma = media = maior = menor = 0
while resposta not in 'N':
    num = int(input('Digite um número: '))
    contador += 1
    soma += num
    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
media = soma / contador
print(f'Você digitou {contador} número(s) e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
