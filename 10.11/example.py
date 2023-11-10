def p(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
        


x = 100
a = []
for i in range(1, int(x**0.5)+1):
    if x % i == 0:
        a.append(i)
        if x // i != i:
            a.append(x//i)

a.sort()
print(a)

print(p(10))