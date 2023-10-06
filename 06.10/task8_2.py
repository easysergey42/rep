from itertools import product

s = "abcdx"
count =0
for i in product(s, repeat=4):
    if i.count("x") == 0 or (i.count("x")==1 and i[0]=="x"):
        count+=1 
print(count)