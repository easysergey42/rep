for x in range(185311, 185330+1):
    h = []
    for i in range(1, int(x**0.5)+1):

        if x % i == 0:
            h.append(i)

            if x//i != i:
                h.append(x//i)

    if len(h) == 4:
        h.sort()
        print(h)
