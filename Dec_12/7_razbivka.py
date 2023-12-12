s = open("Dec_12/24-7.txt").readline()

print(s[:100])

while "AA" in s or "BB" in s or "CC" in s:
    s = s.replace("AA", "A A").replace("BB" , "B B").replace("CC", "C C")

a = s.split()

print(len(max(a, key=len)))