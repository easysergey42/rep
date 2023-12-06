a = [1,2,3,4,5]

b = [x+1 for x in a if x%2==0]

b = []
for x in a:
    if x%2 == 0:
        b.append(x+1)


print(b)