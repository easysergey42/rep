x = 125**5+25**9-30
s = ""
while x !=0:
    y = x%5
    x = x//5
    s += str(y)
s = s.count("4")
print(s)