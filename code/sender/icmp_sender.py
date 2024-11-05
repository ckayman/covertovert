from scapy.all import IP, ICMP, send

# Implement your ICMP sender here

packet = IP(dst="receiver", ttl=1) / ICMP() # actually used the IP address from "ifconfig" output first time, but then thought the IP might change
send(packet)
