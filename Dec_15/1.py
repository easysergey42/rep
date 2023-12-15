f = open('Dec_15/26_1.txt')

n = int(f.readline())

a = []
for i in range(n):
    s, r, t = f.readline().split()
    # s - время в которое приехала машина, r - время, которое она будет стоять на парковке, t - тип машины(A/B)
    a.append([int(s), int(r), t])

a.sort()

# 70 - автомобильных мест и 30 - автобусных. Пусть первые 70 элементов списка - автомобильные места, последние 30 - автобусные
# т.е. park[0]...park[69] - автомобильные
# park[70]...park[99] - автобусные
park = [0] * 100

cntBus = 0
cntFail = 0
for x in a:
    s, r, t = x  # x = [a,b,c]
    if t == "A":
        for j in range(len(park)):
            if park[j] <= s:
                park[j] = s + r
                break
        else:
            cntFail += 1
    elif t == "B":
        for j in range(70, 100):
            if park[j] <= s:
                park[j] = s + r
                cntBus += 1
                break
        else:
            cntFail += 1


print(cntBus, cntFail)
