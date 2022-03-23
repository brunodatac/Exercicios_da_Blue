texto = str(input('Digite um texto: '))
cont_palavras = texto.split()
cont_letras = list(texto.replace(' ',''))

print(f'O texto possui {len(cont_palavras)} palavras e {len(cont_letras)} letras')
