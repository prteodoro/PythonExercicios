exercicio = ' Exercício 011 '
enunciado = 'Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área ' \
            'e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta ' \
            'uma área de 2m².'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

lar = float(input('Digite a largura da parede em m²: '))
alt = float(input('Digite a altura da parede em m²: '))
area = lar * alt
tinta = area / 2
print(f'Essa parede possui uma área de {area}m², e para pintá-la são necessário(s) {tinta:.3f}litro(s) de tinta.')
