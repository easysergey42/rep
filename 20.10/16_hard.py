def f(n):
    if n == 1:
        return 1
    if n >= 2:
        return f(n-1)-g(n-1)


def g(n):
    if n == 1:
        return 1
    if n >= 2:
        return f(n-1) + g(n-1)
    

print(f(5), g(5))