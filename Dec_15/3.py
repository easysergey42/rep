# https://inf-ege.sdamgia.ru/problem?id=36039
f = open('zadanie_26/2.txt')

s, n = map(int, f.readline().split())

a = []
for i in range(n):
    x = int(f.readline())
    a.append(x)

a.sort()

mas = 0
b = []
cnt = 0
for x in a:
    if mas+x > s:
        break  # cnt - id of next => cnt-1 - id poslednego
    mas += x
    cnt += 1
    b.append(x)

print(f'{b[-1]} -> {a[-1]}, nedogruz = {s-mas} ')

for i in range(cnt, len(a)):
    if a[i] <= b[-1]:
        continue
    if mas + (a[i] - b[-1]) > s:
        break
    mas += a[i] - b[-1]
    b[-1] = a[i]

print(len(b), b[-1])
