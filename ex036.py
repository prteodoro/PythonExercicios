exercicio = ' Exercício 036 '
enunciado = """Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa 
vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo 
será negado."""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

valorcasa = float(input('Valor do imóvel: R$\033[32m\033[m'))
salariocomprador = float(input('Salário do comprador: R$'))
anosfinanciamento = int(input('Quantos anos de financiamento? '))
prestacaomensal = valorcasa / anosfinanciamento / 12
prestacaominima = salariocomprador * 30 / 100
print(f'Para pagar uma casa de R${valorcasa:.2f} em {anosfinanciamento:.0f} anos a prestação será '
      f'de R${prestacaomensal:.2f}.')
if prestacaominima < prestacaomensal:
    print(f'Empréstimo \033[31mNEGADO\033[m!')
else:
    print(f'Empréstimo pode ser \033[32mCONCEDIDO\033[m!')

#\033[32m{valor01}\033[m e \033[31m{valor02}\033[m!!!')