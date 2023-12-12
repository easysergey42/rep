s = open('Dec_08/24-2.txt').readline()

# print(indexes[:100])
mini = 10**7
indexes = []

for i in range(len(s)):
    if s[i] == 'U':
        indexes.append(i)

for i in range(len(indexes)-109):
    mini = min(indexes[i+109] - indexes[i]+1, mini)

print(mini)
