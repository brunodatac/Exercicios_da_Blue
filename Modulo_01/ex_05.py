palavra = str(input('Digite uma palavra: ')).replace(' ','')
letras = list(palavra)

for x in range(0, len(palavra), 1):
    if x <= len(palavra) - 1:
        teste = letras[x].isdigit()
        if teste == True:
            print(f'Existe um número na {x + 1}ª posição da palavra')
