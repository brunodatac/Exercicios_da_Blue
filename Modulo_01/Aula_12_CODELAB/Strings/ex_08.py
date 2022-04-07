import re


def senha(nome, ano_de_nasc):
    senha_montada = ano_de_nasc[-2:] + nome [0:2] + ano_de_nasc[0:2] + nome[3:]  
    return senha_montada


nome = str(input('Digite seu nome: '))
ano_de_nasc = str(input('Digite o seu ano de nascimento: '))

if nome == '' or re.findall("[0-9]+", nome):
    raise ValueError('O nome não pode estar vazio ou possuir números.')
elif len(ano_de_nasc) != 4:
    raise ValueError('O ano deve está no formato aaaa.')
else:
     print(senha(nome, ano_de_nasc))
