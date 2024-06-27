exercicio = ' Exercício 066 '
enunciado = """Crie um programa que leia vários números inteiros pelo teclado. O programa só vai 
parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos 
números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

contador = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    contador += 1
    soma += num
print(f'A soma dos {contador} valores foi de {soma}!')
