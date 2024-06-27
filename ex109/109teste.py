import moeda

exercicio = ' Exercício 109 '
enunciado = """Modifique as funções que foram criadas no desafio 107 para que elas aceitem um 
parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela 
função cadastro(), desenvolvida no desafio 108."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valor = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, False)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor)}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10, True)}')
print(f'Diminuindo 5%, temos {moeda.diminuir(valor, 5, True)}')
