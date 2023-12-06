a = [int(x) for x in open('Dec_06/17_2.txt')]
maxi = -10001
cnt = 0 

mini = min([x for x in a if abs(x)%10==3]) ** 2
# mini = min([x for x in a if str(x)[-1] == '3']) ** 2

for i in range (len(a)-1):
    if (a[i]<a[i+1] and abs(a[i])%10==3 and a[i]**2+a[i+1]**2<mini or 
        a[i]>a[i+1] and abs(a[i+1])%10==3 and a[i]**2+a[i+1]**2<mini):
        cnt+=1
        if maxi< a[i]**2+a[i+1]**2:
            maxi = a[i]**2+a[i+1]**2
print(cnt, maxi)
