# c - какой ход по счету был сделан, тогда c+1 - это код, который делается сейчас
def fn(s, c, m):
    if s >= 63:
        return c % 2 == m % 2  # если сделанный ход совпадает по четности (Tr)
    if c == m:
        return 0

    h = [fn(s+1, c+1, m), fn(s+4, c+1, m), fn(s*5, c+1, m)]

    return any(h) if (c+1) % 2 == m % 2 else all(h)

    # if (c+1) % 2 == m % 2:
    #     return any(h)
    # else:
    #     return all(h)

    # if (c+1) % 2 == m % 2:  # если сейчас ходим мы, достаточно, чтобы один из ходов приводил к победе
    #     return fn(s+1, c+1, m) or fn(s+4, c+1, m) or fn(s*5, c+1, m)
    # else:  # если ходим не мы, то необходимо чтобы любой ход соперника приводил к нашей победе
    #     return fn(s+1, c+1, m) and fn(s+4, c+1, m) and fn(s*5, c+1, m)


for s in range(1, 63):
    # for m in range(1, 10):
    #     if fn(s, 0, m):
    #         print(s, m)
    #         break
    if fn(s, 0, 2):
        print(s)


# print(fn(17, 200, 0, 2))
