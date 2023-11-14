def p(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

A = 123456789
B = 223456789
for x in range(int(A**0.25), int(B**0.25)+1):
    if p(x) == True:
        print(x**4, x**3)