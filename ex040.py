exercicio = ' Exercício 040 '
enunciado = """Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem 
no final, de acordo com a média atingida:
	- Média abaixo de 5.0: REPROVADO
	- Média entre 5.0 e 6.9: RECUPERAÇÃO
	- Média 7.0 ou superior: APROVADO"""
fim = '='*30
print(f'{exercicio:=^30} \n{enunciado} \n{fim}')

nota01 = float(input('Primeira nota: '))
nota02 = float(input('Segunda nota: '))
media = (nota01 + nota02) / 2
print(f'Tirando {nota01:.1f} e {nota02:.1f}, a média do aluno é {media:.1f}')
if media >= 7:
    print(f'O aluno está APROVADO.')
elif media < 5:
    print(f'O aluno está REPROVADO.')
else:
    print(f'O aluno está em RECUPERAÇÃO.')
