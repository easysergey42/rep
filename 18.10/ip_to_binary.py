ip = [148, 195, 140, 28]
ip_binary = '.'.join(f'{x:>08b}' for x in ip)
print(ip_binary)

# ip = '148.195.140.28'
# ip_binary = '.'.join(f'{int(x):08b}' for x in ip.split('.'))
# print(ip_binary)
# print(ip)
