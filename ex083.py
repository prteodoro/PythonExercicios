exercicio = ' Exercício 083 '
enunciado = """Crie um programa onde o usuário digite uma expressão qualquer que use 
parênteses. Seu aplicativo deverá analisar se a expressão passada está com os 
parênteses abertos e fechados na ordem correta."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

expressao = str(input('Digite a expressão: '))
lista = []
for pos in expressao:
    if pos == '(':
        lista.append('(')
    elif pos == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')

