texto = str(input('Digite um texto com 6 caracteres: '))

if len(texto) > 6 or len(texto) < 6:
    print('\nERRO! O texto deve possuir 6 caracteres. Tente novamente.')
elif len(texto) == 0:
    print('\nERRO! O texto deve possuir 6 caracteres. Tente novamente.')
else:
    print(f'A primeira letra é {texto[0]}')
    print(f'A segunda letra é {texto[1]}')
    print(f'A terceira letra é {texto[2]}')
    print(f'A quarta letra é {texto[3]}')
    print(f'A quinta letra é {texto[4]}')
    print(f'A sexta letra é {texto[5]}')