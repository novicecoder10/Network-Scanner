from scapy.all import ARP, Ether, srp

target_ip = "192.168.10.2/24" # specify the target IP range

#create an ARP request packet

arp = ARP(pdst=target_ip)

# create an Ethernet frame

ether = Ether(dst="ff:ff:ff:ff:ff:ff") # broadcast MAC address
# combine them into a single packet

packet = ether/arp

result = srp(packet,timeout=3)[0]

# create a list to hold the results

clients = []
# loop through the results

for sent, received in result:
    # for each response, append the IP and MAC address to the list
    clients.append({'ip':received.psrc, 'mac':received.hwsrc})
# print the results
print("IP Address\t\tMAC Address")
print("-----------------------------------------")

for client in clients:
    print("{:16}  {}".format(client['ip'], client['mac']))
