s = open('Dec_12/24-3.txt').readline()

c = 0
m = 0
for i in range(len(s)): # бежим по индексам
    if s[i] == "C":
        c += 1
        m = max(m, c) 
    else:
        c = 0

print(m)
