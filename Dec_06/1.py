a = [int(x) for x in open('Dec_06/17_1.txt')]


mini = min([x for x in a if x % 10 == 3 and len(str(x)) == 3])
# mini = 200001
# for x in a:
#     if x % 10 == 3 and len(str(x)) == 3:
#         mini = min(mini, x)

cnt = 0
maxi = 0
ans = []
for i in range(len(a)-1):
    if len(str(a[i])) == 4 and len(str(a[i+1])) != 4 or len(str(a[i+1])) == 4 and len(str(a[i])) != 4:
        if (a[i]**2 + a[i+1]**2) % mini == 0:
            maxi = max(a[i]**2 + a[i+1]**2, maxi)
            cnt += 1
            ans.append(a[i]**2 + a[i+1]**2)


print(cnt, maxi)
print(len(ans), max(ans))
