import random
import numpy as np


def todas_as_rodadas(rodadas, jogadores):
    texto = ''
    if rodadas < 1:
        texto += 'É necessario ter pelo menos uma rodada para o jogo acontecer!'
    elif jogadores < 2:
        texto += 'É necessario ter pelo menos dois jogares competindo para o jogo acontecer!'

    else:
        for turno in range(rodadas):
            resultado_dos_dados = jogada_de_dados(jogadores)
            texto += f'\nRodada: {turno + 1}\n'

            for jogador in range(len(resultado_dos_dados)):
                texto += f'Jogador N.{jogador + 1} fez: {resultado_dos_dados[jogador]}\n'
            pontos_por_jogador(resultado_dos_dados)

        if pontos.count(np.max(pontos)) == 1:
            texto += str(f"\nO Jogador N.{pontos.index(np.max(pontos))+1} "
                         f"ganhou {np.max(pontos)} rodadas e é o VENCEDOR!")
        else:
            texto += "\nEMPATE! Ninguém venceu."
    return texto


def jogada_de_dados(jogadores):
    resultados = []
    for x in range(jogadores):
        dados = random.randint(1, 6)
        resultados.append(dados)
    return resultados


def pontos_por_jogador(resultado_dos_dados):
    maior_resultado = np.max(resultado_dos_dados)
    repeticoes_do_maior_resultado = resultado_dos_dados.count(maior_resultado)
    for x in range(len(resultado_dos_dados)):
        if resultado_dos_dados[x] == maior_resultado and repeticoes_do_maior_resultado == 1:
            pontos[x] += 1
    return pontos


def lista_de_pontuacao(jogadores):
    for x in range(jogadores):
        pontos.append(0)
    return pontos


pontos = []

numero_de_rodadas = int(input("Quantas rodadas deseja jogar? "))
numero_de_jogadores = int(input("Quantos jogadores? "))
lista_de_pontuacao(numero_de_jogadores)
print(todas_as_rodadas(numero_de_rodadas, numero_de_jogadores))
