primeiro_numero = input("Digite o primeiro número: ")
segundo_numero = input("Digite o segundo número: ")

if primeiro_numero == segundo_numero:
    print(f'Os número {primeiro_numero} e {segundo_numero} são IGUAIS!')
elif primeiro_numero > segundo_numero:
    print((f'O número {primeiro_numero} é MAIOR que o {segundo_numero}!'))
else:
    print((f'O número {segundo_numero} é MAIOR que o {primeiro_numero}!'))
