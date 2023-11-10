maxcnt = 0
chislo = 0

for x in range(120115, 120201):
    cnt = 0
    for i in range(1, int(x**0.5)+1):

        if x % i == 0:
            cnt += 1

            if x // i != i:
                cnt += 1

    if cnt >= maxcnt:
        maxcnt = cnt
        chislo = x

print(maxcnt, x)
