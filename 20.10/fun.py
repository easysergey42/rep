#про функции

# def f(x):
#     return x+1

# def f2(x):
#     return 10

# n! = n*(n-1)*(n-2)*...*1
# 2! = 2 * 1
# 3! = 3 * 2 * 1
# 4! = 4 * 3!
# n! = n * (n-1)!
# import sys
# sys.setrecursionlimit(3000)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(1000))