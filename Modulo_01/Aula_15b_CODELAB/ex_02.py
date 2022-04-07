def num_primos (num):
    contador_multiplos = 0
    for i in range(2, num):
        if num % i == 0:
            contador_multiplos += 1
    if num == 1:
        return('O número 1 não é um número primo!')    
    elif contador_multiplos == 0:
        return(f'O numero {num} é primo!')
    else:
        return(f'Tem {contador_multiplos} multiplos acima de 2 e abaixo de {num}. Então o número {num} não é primo!')


valor = int(input('Digite um número e descubra se ele é um numero primo: '))
print(num_primos(valor))
