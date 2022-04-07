from datetime import date
print("Descubra se você já está apto para votar!")
ano_de_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today()
idade = ano_atual.year - ano_de_nascimento

if 18 <= idade <= 70:
    print(f"\nEleitores com idade entre 18 e 70 anos são obrigados por lei a votar.\nComo você tem {idade} anos, o "
          f"seu voto é OBRIGATORIO.")
elif 18 > idade >= 16 or idade > 70:
    print(f"\nEleitores com idade entre 16 e 17 anos ou mais de 70 anos não tem obrigatoriedade de votar.\nComo você "
          f"tem {idade} anos, o seu voto ainda é OPCIONAL.")
else:
    print(f"\nPessoas com menos de 16 anos não podem votar .\nComo você tem {idade} anos, o seu voto é NEGADO.")


