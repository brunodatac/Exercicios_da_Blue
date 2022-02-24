print('\nSão permitidos saques apartir de R$ 10.00 até R$ 600.00')
valor = int(input('Digite o valor do saque: '))

cem = int(valor / 100)
valor = valor % 100

cinq = int(valor / 50)
valor = valor % 50

dez = int(valor / 10)
valor = valor % 10

cinco = int(valor / 5)
valor = valor % 5

um = valor

print(f'Notas R$100,00 =  {cem}\nNotas R$ 50,00 =  {cinq}\nNotas R$ 10,00 =  {dez}\nNotas R$  5,00 =  {cinco}\nNotas R$  1,00 =  {um}')
