import random
novamente = True

while novamente == True:
    rodadas = int(input("Vamos jogar quantas rodadas? "))

    print("VAMOS JOGAR JOKENPO")

    cont = 1
    pontos = 1
    pontos_pc = 1

    for x in range(0, rodadas, 1):
        cont += 1
        print("\nOpções:\nPedra\nPapel\nTesoura\n")
        jg = input("Qual a sua escolha? ").upper()

        lista = ["PEDRA", "PAPEL", "TESOURA"]
        pc = random.choice(lista)

        print(f"\nVocê escolheu: {jg} | Computador escolheu: {pc}")

        if jg == 'PEDRA' and pc == 'TESOURA':
            pontos += 1
            print("***VOCÊ VENCEU!***")
        elif jg == 'PAPEL' and pc == 'PEDRA':
            pontos += 1
            print("***VOCÊ VENCEU!***")
        elif jg == 'TESOURA' and pc == 'PAPEL':
            pontos += 1
            print("***VOCÊ VENCEU!***")
        elif jg == pc:
            print("*EMPATOU!*")
        else:
            pontos_pc += 1
            print("~~~VOCÊ PERDEU!~~~")

    print(f"\nPLACAR:\nVocê fez {pontos - 1} pontos\nComputador fez {pontos_pc - 1} pontos")
    if pontos > pontos_pc:
        print("\nJogador venceu!")
    else:
        print("\nNPC venceu!")
    print("\nGostaria de jogar novamente?")

    jogar_novamente = str(input("Sim/Não: ")).upper()
    if jogar_novamente == 'SIM' or 'S' in jogar_novamente:
        novamente = True

    elif jogar_novamente == 'NAO' or 'N' in jogar_novamente:
        print("\nFIM DE JOGO!")
        novamente = False

