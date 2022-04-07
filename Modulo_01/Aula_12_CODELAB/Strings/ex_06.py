palavra = str(input('Digite uma palavra: '))
numero = int(input('Digite um número: '))
corte = slice(numero)

if numero > len(palavra) or numero == 0:
    print('ERRO! Esse valor não pode ser aplicado ao comprimento da palavra!')
else:
    print(palavra[corte])