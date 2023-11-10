# ip = [148, 195, 140, 28]
# ip_binary = '.'.join(f'{x:>08b}' for x in  [148, 195, 140, 28])
# print(ip_binary)

ip = '98.162.78.139'
ip_binary = '.'.join(f'{int(x):08b}' for x in ip.split('.'))
print(ip)
print(ip_binary)

ip = '98.162.78.154'
ip_binary = '.'.join(f'{int(x):08b}' for x in ip.split('.'))
print(ip)
print(ip_binary)

