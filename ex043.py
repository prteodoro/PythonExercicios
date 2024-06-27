exercicio = ' Exercício 043 '
enunciado = """Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e 
mostre seu status, de acordo com a tabela abaixo:
	- Abaixo de 18.5: Abaixo do Peso
	- Entre 18.5 e 25: Peso ideal
	- 25 até 30: Sobrepeso
	- 30 até 40: Obesidade
	- Acima de 40: Obesidade mórbida"""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura * altura)
print(f'O IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print(f'Você está ABAIXO DO PESO normal!')
elif imc < 25:
    print(f'PARABÉNS, você está na faixa de PESO NORMAL!')
elif imc < 30:
    print(f'Você está com SOBREPESO!')
elif imc < 40:
    print(f'Você está em OBESIDADE!')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
