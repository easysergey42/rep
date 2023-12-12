s = open('Dec_12/24-3.txt').readline()
s = s.replace('A', ' ').replace('B', ' ')
a = s.split()

print(len(max(a, key=len)))
