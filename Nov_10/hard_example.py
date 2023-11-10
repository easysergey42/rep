a = []

for x in range(10):
    a.append(int(f'3{x}4583'))
    
    for y in range(10):
        a.append(int(f'3{x}458{y}3'))

    for y in range(100):
        a.append(int(f'3{x}458{y:02}3'))

    for y in range(1000):
        a.append(int(f'3{x}458{y:03}3'))

print(a[200:300])
