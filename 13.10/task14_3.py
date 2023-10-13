ab = '0123456789abc'

mini = 99999999999999
for x in ab:
    for l in ab:
        y = int('8'+x+'78'+l, 13)
        z = int('79' + x + l +'7', 18)
        if (y+z)%9==0:
            if (y+z) < mini:
                mini = (y+z)
                print((y+z)//9)

