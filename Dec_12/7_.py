s = open("Dec_12/24-7.txt").readline()

c = m = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        c += 1
        m = max(m, c)
    else:
        c = 1

print(m)
