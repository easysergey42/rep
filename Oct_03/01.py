count = 0
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    count += 1
                    if (count == 1020):
                        print(a,b,c,d,e)