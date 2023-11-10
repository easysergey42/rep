import sys 
sys.setrecursionlimit(3000)
def f(n):
    if n == 1:
        return n
    if n > 1:
        return n - 1 + f(n-1)
    

    

# f(2024) = 2023 + f(2023) = 2023 + 2022 + f(2022)
# f(2023) = 2022 + f(2022)
# f(2024) - f(2022) = 2023 + 2022 + f(2022) - f(2022)
print(f(2024)-f(2022))