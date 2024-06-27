import moeda

exercicio = ' Exercício 108 '
enunciado = """Adapte o código do desafio 107, criando uma função adicional chamada cadastro() que consiga 
mostrar os valores como um valor monetário formatado."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(valor, 10))}')
print(f'Diminuindo 5%, temos {moeda.moeda(moeda.diminuir(valor))}')
