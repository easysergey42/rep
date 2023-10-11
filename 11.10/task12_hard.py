
for i in range(3, 10001):
    s = "5"
    l = "2" * i
    s += l
    while "52" in s or "1122" in s or "2222" in s:
        if "52" in s:
            s = s.replace("52", "1", 1)

        if "2222" in s:
            s = s.replace("2222", "5", 1)

        if "1122" in s:
            s = s.replace("1122", "25", 1)

    sum = 0
    for j in s:
        sum += int(j)

    if sum == 88:
        print(i)
        break
