numero = int(input("Digite um número para saber se ele é Par ou Ímpar: "))
res = numero % 2

if res == 0:
    print(f'O número {numero} é PAR!')
else:
    print(f'O número {numero} é ÍMPAR!')
