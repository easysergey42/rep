f = open('Dec_15/26_2.txt')

n = int(f.readline())

a = []

for i in range(n):
    start, end = f.readline().split()
    a.append([int(end), int(start)])

a.sort()

print(a[:10])