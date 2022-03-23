palavra = str(input('Digite uma palavra: ')).replace(' ','')
letras = list(palavra)

for x in range(0, len(palavra), 1):
    if x <= len(palavra) - 1:
        descoberta_de_numeros = letras[x].isdigit()
        if descoberta_de_numeros == True:
            print(f'Existe um número na {x + 1}ª posição da palavra')
