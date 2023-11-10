from ipaddress import * 

ip = '111.81.208.27'
net_addr = '111.81.192.0'

for mask in range(33):
    net = ip_network(f'{ip}/{mask}',0)
    if str(net.network_address) == net_addr:
        print(net, net.netmask)

