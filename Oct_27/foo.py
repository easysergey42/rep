def fn(s1, s2, m):
    if s1+s2 >= 231:
        return m % 2 == 0
    if m == 0:
        return False
    h = [fn(s1+2, s2, m-1), fn(s1*2, s2, m-1),
         fn(s1, s2+2, m-1), fn(s1, s2*2, m-1)]
    return any(h) if (m-1) % 2 == 0 else all(h)




print('20)', [i for i in range(1, 214) if fn(17, i, 3) and not fn(17, i, 1)])

print('21)', [i for i in range(1, 214) if fn(17, i, 4) and not fn(17, i, 2)])
