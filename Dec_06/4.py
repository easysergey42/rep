a = [int(x) for x in open('Dec_06/17_4.txt')]

cnt = 0
maxi = -1

for i in range(len(a)-1):
    if (a[i]%3==0 or a[i+1]%3 == 0) and (a[i]+a[i+1])%5 == 0:
        cnt += 1
        maxi = max(maxi, a[i]+a[i+1])

print(cnt, maxi)