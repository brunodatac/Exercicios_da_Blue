valor = float(input("Digite o valor para conversão: R$ "))

dolar = valor / 5.16
euro = valor / 5.75
libra_esterlina = valor / 6.89
dolar_canadense = valor / 4.07
peso_argentino = valor / 0.048
peso_chileno = valor / 0.0064

print(f'\nDolar: $ {dolar:.2f}\nEuro: € {euro:.2f}\nLibra Esterlina: £{libra_esterlina:.2f}\nDolar Canadense: '
      f'$ {dolar_canadense:.2f}\nPeso Argentino: $ {peso_argentino:.2f}\nPeso Chileno: $ {peso_chileno:.2f}')
