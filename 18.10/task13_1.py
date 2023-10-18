from ipaddress import *


net = ip_network('98.162.78.139/28', 0)


# print(net, net.netmask)
for mask in range(33):
    net1 = ip_network(f'98.162.78.139/{mask}',0)
    net2 = ip_network(f'98.162.78.154/{mask}',0)
    if net1 != net2:
        print(mask)
