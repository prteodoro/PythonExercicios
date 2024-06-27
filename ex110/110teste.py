import moeda

exercicio = ' Exercício 110 '
enunciado = """Adicione ao módulo cadastro.py criado nos desafios anteriores, uma função chamada resumo(), 
que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valor = float(input('Digite o preço: R$'))
moeda.resumo(valor, 20, 12)

