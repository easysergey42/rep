s = open('Dec_12/24-1.txt').readline()
s = s.replace("A", " ")
a = s.split()

maxi = 0
for x in a:
    if x.count("E") >= 3:
        if len(x) > maxi:
            maxi = len(x)

print(maxi)
