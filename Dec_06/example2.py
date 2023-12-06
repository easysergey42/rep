
a = "ABCD"

for i in range (len(a)-1):
    for j in range(i+1, len(a)):
        print(a[i],a[j])

print("======================")
for i in range (len(a)):
    for j in range(len(a)):
        if i < j:
            print(a[i],a[j])