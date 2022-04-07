palavra = str(input('Digite uma palavra: ')).lower()
frase = str(input('Digite uma frase: ')).lower()

if palavra in frase:
    print('True')
else:
    print('False')
    