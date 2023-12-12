s = open("Dec_12/24-6.txt").readline()

# c=m=0
# for i in range(0,len(s)-1,2):
#     if (s[i] in "CDF") and (s[i+1] in "AO"):
#         c+=1
#         m = max(m,c)
#     else:
#         c = 0

# for i in range(1,len(s)-1,2):
#     if (s[i] in "CDF") and (s[i+1] in "AO"):
#         c+=1
#         m = max(m,c)
#     else:
#         c = 0

# print(m)



c=0
m=0
i=0
while i < len(s):
    if (s[i] in "CDF") and (s[i+1] in "AO"):
        c+=1
        i+=2
        m = max(m,c)
    else:
        c=0
        i+=1
print(m)