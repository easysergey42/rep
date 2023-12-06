a = [int(x) for x in open('Dec_06/17_3.txt')]

maxi = -1 
cnt = 0
for i in range (len(a)-1):
    for j in range(i+1, len(a)):
        if (a[i]*a[j])%26==0:
            cnt+=1
            if maxi <a[i]+a[j]:
                maxi =a[i]+a[j]
print(cnt,maxi)