exercicio = ' Exercício 007 '
enunciado = 'Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.'
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
#print(f'\nA média entre {nota1} e {nota2} é {media:.1f}')
print(f'\nA média entre {nota1} e {nota2} é {((nota1 + nota2) / 2):.1f}')

