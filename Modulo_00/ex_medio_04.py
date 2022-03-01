nota = float(input('Digite a nota do aluno: '))

if nota < 6.0:
    print('O aluno tirou nota F.')
elif nota < 7.0:
    print('O aluno tirou nota D.')
elif nota < 8.0:
    print('O aluno tirou nota C.')
elif nota < 9.0:
    print('O aluno tirou nota B.')
elif nota <= 10.0:
    print('O aluno tirou nota A.')
else:
    print('Digite um valor entre 0.00 e 10.0 para saber se o aluno foi aprovado.')
