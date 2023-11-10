ab = '0123456789abcde'

for x in ab:
    y = int('97968'+x+'13', 15)
    z = int('7' + x + '213', 15)
    if (y+z) % 14 == 0:
        print(x)
        print((y+z) // 14)
    