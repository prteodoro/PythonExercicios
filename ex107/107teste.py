import moeda

exercicio = ' Exercício 107 '
enunciado = """Crie um módulo chamado cadastro.py que tenha as funções incorporadas aumentar(), 
diminuir(), dobro() e metade.
Faça também um programa que importe esse módulo e use algumas dessas funções."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valor = float(input('Digite o preço: R$'))
print(f'A metade de R${valor} é R${moeda.metade(valor)}')
print(f'O dobro de R${valor} é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor)}')
print(f'Diminuindo 5%, temos R${moeda.diminuir(valor)}')
