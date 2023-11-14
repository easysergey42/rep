def p(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False


x = 100
a = set()
for i in range(1, int(x**0.5)+1):
    if x % i == 0:
        a.add(i)
        a.add(x//i)

# a.sort()
print(sorted(a))

# print(p(10))
