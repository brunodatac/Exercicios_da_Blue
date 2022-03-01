salario = float(input("Salário atual: R$ "))

if salario < 280:
    aumento = salario * 0.2 + salario
    print(f'O seu salário era de R$ {salario:.2f}\nE com o reajuste de 20%ficou R$ {aumento:.2f}')
elif salario < 700:
    aumento = salario * 0.15 + salario
    print(f'O seu salário era de R$ {salario:.2f}\nE com o reajuste de 15% ficou R$ {aumento:.2f}')
elif salario < 1500:
    aumento = salario * 0.10 + salario
    print(f'O seu salário era de R$ {salario:.2f}\nE com o reajuste de 10% ficou R$ {aumento:.2f}')
else:
    aumento = salario * 0.05 + salario
    print(f'O seu salário era de R$ {salario:.2f}\nE com o reajuste de 5% ficou R$ {aumento:.2f}')
