from datetime import date

ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = date.today()
idade = ano_atual.year - ano_nasc

if idade < 15:
    print(f'Você tem apenas {idade} anos e ainda não chegou na Flor da Idade!')
elif idade < 18:
    print(f'Você tem apenas {idade} anos. Você ainda está na Flor da Idade!')
else:
    print(f'Você tem {idade} anos e já passou da Flor da Idade!')
