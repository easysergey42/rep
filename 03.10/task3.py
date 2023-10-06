from itertools import product
alphabet = '0123456'
prod = product(alphabet, repeat=4)

count = 0
for i in prod:
    if i[0] > i[1] and i[1] > i[2] and i[2] > i[3]:
        count += 1
        print(i)

print(count)

# https://inf-ege.sdamgia.ru/problem?id=58237
