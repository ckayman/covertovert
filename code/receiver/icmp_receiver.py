from scapy.all import IP, ICMP, sniff
import sys

# Implement your ICMP receiver here

def pick(packet):
    if packet.haslayer(ICMP) and packet[IP].ttl == 1: # receiving ICMP packet whose TTL value is 1 
        packet.show()
        sys.exit(0)

sniff(filter="icmp", prn=pick) 
# tried using count=1 here, but it still terminates after 
# an "incorrect" packet (e.g. a ttl=2), so a stop filter is added
# edit: stop_filter made it printing the packet twice, so
# imported sys to simply exit, saw no restrictions about it 
# (in the discussion forum it is stated that it should terminate)
