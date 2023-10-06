from itertools import product

alphabet = 'УЧЕНИК'
startSymbols = 'xz'
endSymbols = 'abcde'
prod = product(alphabet, repeat=5)

count = 0
for i in prod:
    # print(i)
    if i[0] == 'У' and i[-1] == 'К':
        count += 1
        # print(i)

print(count)

# https://inf-ege.sdamgia.ru/problem?id=7306