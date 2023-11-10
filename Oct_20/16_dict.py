d = {1 : 1}

for i in range(2, 2024 + 1):
    d[i] = i-1 + d[i-1]

print(d[2024] - d[2022])