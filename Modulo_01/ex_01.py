from math import floor

nome = str(input('Digite um nome: '))
lista = list(nome)
corte = floor((len(nome) / 2))

print(lista[0], lista[corte], lista[len(nome) - 1])
