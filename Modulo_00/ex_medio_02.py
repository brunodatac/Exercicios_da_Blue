
valor = float(input('Digite um valor para saber se é positivo ou negativo: '))

if valor < 0.0:
    print(f'O valor {valor:.1f} é NEGATIVO.')
elif valor > 0.0:
    print(f'O valor {valor:.1f} é POSITIVO')
else:
    print('O valor 0 não é aceito')
