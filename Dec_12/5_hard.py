s = open('Dec_08/24-5.txt').readline()

# print(s[:100])

c = m = 2
for i in range(len(s) - 2):
    if int(s[i]) + int(s[i+1]) > int(s[i+2]):
        c+=1

        if c > m:
            m = c
    else:
        c = 2

print(m)
