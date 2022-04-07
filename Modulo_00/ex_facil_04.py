print('Menu\n\n[1] Prato do dia\n[2] Prato do chefe\n[3] Degustação\n')
escolha = int(input("Digite o número da sua escolha: "))

if escolha == 1:
    print("\nVocê escolheu *Prato do dia*")
elif escolha == 2:
    print("\nVocê escolheu *Prato do chefe*")
elif escolha == 3:
    print("\nVocê escolheu *Degustação*")
else:
    print("Tente novamente!")
