exercicio = ' Exercício 044 '
enunciado = """Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu 
preço normal e condição de pagamento:
	- À vista dinheiro/cheque: 10% de desconto
	- À vista no cartão: 5% de desconto
	- Em até 2x no cartão: preço normal
	- 3x ou mais no cartão: 20% de juros"""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

print(f'{" LOJAS GUANABARA ":=^46}')
valorcompras = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque -10%
[ 2 ] à vista cartão -5%
[ 3 ] 2x no cartão SEM JUROS
[ 4 ] 3x ou mais no cartão COM JUROS""")
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = valorcompras - valorcompras * 10 / 100
elif opcao == 2:
    total = valorcompras - valorcompras * 5 / 100
elif opcao == 3:
    total = valorcompras
    print(f'Sua compra será parcelada em 2x de R${valorcompras / 2:.2f} SEM JUROS.')
elif opcao == 4:
    qtdparcelas = int(input('Quantas parcelas? '))
    total = valorcompras + valorcompras * 20 / 100
    print(f'Sua compra será parcelada em {qtdparcelas}x de R${total / qtdparcelas:.2f} COM JUROS.')
else:
    total = valorcompras
    print(f'Opção INVÁLIDA. Tente novamente!')
print(f'Sua compra de R${valorcompras:.2f} vai custar R${total:.2f} no final.')
