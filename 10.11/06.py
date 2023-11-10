from fnmatch import fnmatch

for i in range (317,100000000+1,317):
    if fnmatch(str(i),"12??1*56"):
        print(i, i//317)

