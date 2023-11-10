
for x in range(125256, 125330+1):
    a = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:

            if i % 2 == 0:
                a.append(i)

            if x // i != i and (x//i) % 2 == 0:
                a.append(x//i)

    if len(a) == 6:
        a.sort()
        print(a)
