from itertools import product

alphabet = '01234567'
even = '0246'
odd = '1357'
count = 0

for i in product(alphabet, repeat=5):
    flag = 1
    for k in range(1, len(i)):
        if ((i[k-1] in even and i[k] in even) or (i[k-1] in odd and i[k] in odd)):
            flag = 0
            break
    for j in alphabet:
        if i.count('1') > 0 or i.count(j) > 1:
            flag = 0
            break
    if flag:
        count += 1
        print(i)

print(count)
