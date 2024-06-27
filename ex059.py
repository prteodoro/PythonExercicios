from time import sleep

exercicio = ' Exercício 059 '
enunciado = """Crie um programa que leia dois valores e mostre um menu na tela:
	[1] somar
	[2] multiplicar
	[3] maior
	[4] novos números
	[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valor01 = int(input('Primeiro valor: '))
valor02 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('=-' * 20)
    print("""        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa""")
    opcao = int(input('>>>> Qual é a sua opção? '))
    if opcao == 1:
        print(f'A soma entre {valor01} + {valor02} é {valor01 + valor02}')
    elif opcao == 2:
        print(f'A multiplicação entre {valor01} x {valor02} é {valor01 * valor02}')
    elif opcao == 3:
        if valor01 > valor02:
            maior = valor01
        else:
            maior = valor02
        print(f'Entre {valor01} e {valor02} o maior valor é {maior}')
    elif opcao == 4:
        print('Informe os números novamente:')
        valor01 = int(input('Primeiro valor: '))
        valor02 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(1.5)
print('=-'*20)
print('Fim do programa! Volte sempre!')