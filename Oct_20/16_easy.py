# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(1) = 1
# F(n) = F(n–1) * n, при n >1
# Чему равно значение функции F(5)? В ответе запишите только натуральное число.

def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) * n
    
print(f(5))