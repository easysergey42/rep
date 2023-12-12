s = open("Dec_08/24-4.txt").readline()
s = s.split("D")
s = s[1:-1]

m = 0
c = 1
for i in s:
    if i.count("O") <= 2:
        c += len(i) + 1
        m = max(m,c)
    else:
        c = 1

print(m)