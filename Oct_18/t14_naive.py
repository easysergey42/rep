for i in range(0, 10000):
    s = '5' + '2'*i
    start=s
    #               -1          -4          
# 522222222... -> 112222222..;115222.. -> 111122..;111152..;
# ..1522222... -> ..1115... (пока есть 5 двоек)
# т.е. за каждые 5 двоек получаем 2 единицы(слева) в итоговую сумму
# case ..52222  -> ..11222;..252 -> ..211 (i.e. if n%5==4 за остаток двоек мы получаем +4)
# case ..5222 -> ..1122;..25 (i.e. n%5==3 -> + 7)
# case ..522 -> ..112 (i.e. n%5==2 -> +4)
# case ..52 -> ..11 (i.e. n%5==1 -> +2)
# case ..5 (n%5 == 0 -> +5)
# x -> x // 5 * 2 + dict[x%5]
    while '52' in s or '2222' in s or '1122' in s:
        if '52' in s: s = s.replace('52', '11', 1)
        if '2222' in s: s = s.replace('2222', '5', 1)
        if '1122' in s: s = s.replace('1122', '25', 1)

    summ = 0
    for x in s:
        summ += int(x)
    if summ == 64:
        print(f'{i} is answer')
    # print(f'{i}:\tInput: {start}\n\t\tOutput: {s} ({summ})')
    # print(f'{i}:\tOutput: {s} ({summ})')
