from math import floor

nome = list(input('Digite um nome: '))
corte = floor((len(nome) / 2))

print(nome[0] + nome[corte] + nome[len(nome) - 1])
