exercicio = ' Exercício 077 '
enunciado = """Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""
fim = '='*50
print(f'{exercicio:=^50} \n{enunciado} \n{fim}')

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar',
            'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos a vogal: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
