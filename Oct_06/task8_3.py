from itertools import product

alphabet = "01234567"
even = "0246"
odd = "1357"
count = 0
for i in product(alphabet, repeat=5):
    flag = True
    for j in alphabet:
        if (i.count(j) > 1):
            flag = False

    for j in range(1, len(i)): #Пробегаемся по слову 
        if i[j-1] in even and i[j] in even:
            flag = False
        if i[j-1] in odd and i[j] in odd:
            flag = False
    
    if flag == True :
        count += 1

print(count)