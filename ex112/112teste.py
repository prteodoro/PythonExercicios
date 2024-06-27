from utilidadesCeV import moeda, dado

exercicio = ' Exercício 112 '
enunciado = """Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. 
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma 
validação de dados para aceitar apenas valores que sejam monetários."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valor = dado.leiaDinheiro('Digite o preço: ')
moeda.resumo(valor, 20, 12)

