def fn(s1,s2, c, m):
    if s1+s2 >= 45:
        return c % 2 == m % 2 
    if c == m:
        return 0

    h = [fn(s1+s2,s2, c+1, m), fn(s1, s2+s1,c+1, m)]

    return any(h) if (c+1) % 2 == m % 2 else all(h)

for i in range(1,38):
    if fn(i,i,0,4)==1 and fn(i,i,0,2)==0:
        print(i)
    
