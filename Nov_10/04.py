from fnmatch import fnmatch

for x in range(2622, 10**8 + 1, 2622):
    if fnmatch(str(x), "1?4*6?8"):
        print(x, x//2622)
