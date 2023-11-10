from itertools import product
alphabet = 'abcdexz'
startSymbols = 'xz'
endSymbols = 'abcde'
prod = product(alphabet, repeat=4)

count = 0
for i in prod:
    if (i[0] in startSymbols and
            i[1] in startSymbols and
            i[2] in endSymbols and
            i[3] in endSymbols):

        count += 1

print(count)


# https://inf-ege.sdamgia.ru/problem?id=14225
