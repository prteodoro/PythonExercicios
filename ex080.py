exercicio = ' Exercício 080 '
enunciado = """Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-os em uma lista, já na posição correta de inserção(sem usar o sort()).
No final, mostre a lista ordenada na tela."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

valores = []
for cont in range(0, 5):
    num = int(input('Digite um valor: '))

    if cont == 0 or num >= max(valores):
        valores.append(num)
        print('Adicionado ao final da lista...')
    else:
        posicaonum = len(valores)
        for pos, valor in enumerate(valores):
            if num < valor:
                if posicaonum >= pos:
                    posicaonum = pos
        valores.insert(posicaonum, num)
        print(f'Adicionado na posição {posicaonum} da lista...')
        # SOLUÇÃO DOIS COM WHILE DENTRO DESSE MESMO ELSE:
        #       pos = 0
        #       while pos < len(valores):
        #           if num <= valores[pos]:
        #               valores.insert(pos, num)
        #               print(f'Adicionado na posição {pos} da lista...')
        #               break
        #           pos += 1
print('-='*25)
print(f'Os valores digitados em ordem foram {valores}')
