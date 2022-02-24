import random
import numpy as np


def todas_as_rodadas(rodadas, quantidade_de_jogadores):
    saida = ''
    if rodadas < 1:
        saida += str('É necessario ter pelo menos 1 rodada para o jogo acontecer!')
    elif quantidade_de_jogadores < 2:
        saida += str('É necessario ter pelo menos 2 jogares competindo para o jogo acontecer!')

    else:
        for turno in range(rodadas):
            pontuacao_obtida = pontuacao_de_cada_rodada(quantidade_de_jogadores)
            saida += (f'\nRodada: {turno + 1}\n')

            for jogador in range(len(pontuacao_obtida)):
                saida += (f'Jogador N.{jogador + 1} fez: {pontuacao_obtida[jogador]}\n')
            grande_vencedor(pontuacao_obtida)

        if pontos.count(np.max(pontos)) == 1:
            saida += str(f"\nO Jogador N.{pontos.index(np.max(pontos))+1} ganhou {np.max(pontos)} rodadas e é o VENCEDOR!")
        else:
            saida += str("\nEMPATE! Ninguém venceu.")
    return saida


def pontuacao_de_cada_rodada(pontuacao_por_jogador):
    resultados = []
    for x in range(pontuacao_por_jogador):
        dados = random.randint(1, 6)
        resultados.append(dados)
    return resultados


def grande_vencedor(pontos_da_rodada):
    maior_valor = np.max(pontos_da_rodada)
    y = pontos_da_rodada.count(maior_valor)
    for x in range(len(pontos_da_rodada)):
        if pontos_da_rodada[x] == maior_valor and y == 1:
            pontos[x] += 1
    return pontos


def pontuacoes(pontuacao):
    for x in range(pontuacao):
        pontos.append(0)
    return pontos


inicio = True
pontos = []

while inicio:
    rodadas = int(input("Quantas rodadas deseja jogar? "))
    quantidade_de_jogadores = int(input("Quantos jogadores? "))
    pontuacoes(quantidade_de_jogadores)
    print(todas_as_rodadas(rodadas, quantidade_de_jogadores))

    recomecar = input(str("Deseja jogar novamente?(S/N) ")).lower()
    if recomecar == 'n':
        print('FIM DO JOGO!')
        inicio = False
