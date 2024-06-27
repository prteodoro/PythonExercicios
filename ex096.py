exercicio = ' Exercício 096 '
enunciado = """Faça um programa que tenha uma função chamada área(), que receba as dimensões 
de um terreno retangular (largura e comprimento) e mostre a área do terreno."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

print(f'  Controle de Terrenos ')
print('-'*30)


def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')


largura = float(input('LARGURA (m²): '))
comprimento = float(input('COMPRIMENTO (m²): '))
area(largura, comprimento)
