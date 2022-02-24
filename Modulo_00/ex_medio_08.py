n1 = 1
t = 1

while n1 <= 10:
    mult = n1 * t
    t += 1
    if t == 11:
        t = 1
        n1 += 1
    print(mult)
