print("Digite 5 números inteiros!")
lst = []

for x in range(1, 6):
    add = int(input(f"{x}º número: "))
    lst.append(add)
    lst = sorted(set(lst))

print(lst)
