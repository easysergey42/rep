def p(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


A = 101000000
B = 102000000
for x in range(int((A/2) ** 0.5), int((B/2)**0.5)+1):
    if p(x) == True:
        print(2 * x ** 2)
