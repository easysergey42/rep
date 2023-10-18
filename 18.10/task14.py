
x = 3 * 3125**8 + 2 * 625**7 - 4 * 625**6 + 3 * 125**5 - 2*25**4 -2024

count = 0
while x > 0:
    i = x % 25
    if (i == 0):
        count+=1
    x = x // 25

print(count)