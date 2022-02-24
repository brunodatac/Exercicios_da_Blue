from random import randint
npc = randint(0, 10)
print("Tente adivinhar qual número inteiro o Computador escolheu entre 0 e 10!")
player = int(input("Digite a sua escolha: "))
print(f"\nVocê escolheu o número: {player}\nO Computado escolheu o número: {npc}")

if player != npc:
    print("\n***O Computador venceu!***")
else:
    print("\n***Você venceu!***")
