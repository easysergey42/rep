import matplotlib.pyplot as plt
d = dict()
d[0] = 5
d[1] = 2
d[2] = 4
d[3] = 7
d[4] = 4

def f(n):
    """Возвращает сумму цифр в выходной строке
    
    Входная = '5' + '2' * n
    """
    return (n // 5) * 2 + d[n%5]


x = range(0,100)
y = [f(i) for i in x]

plt.plot(x, y)  # Построение графика
plt.xlabel('X-Axis')  # Подпись оси x
plt.ylabel('Y-Axis')  # Подпись оси y
plt.title('Graph of f(x) = x^2')  # Заголовок графика
plt.grid(True)  # Отображение сетки
# plt.show()  # Показать график



for n in range(0,10000):
    # print(n, f(n))
    if f(n) == 64:
        print(n, f(n))

    if f(n) >= 68:
        print(n, "too much")
        break