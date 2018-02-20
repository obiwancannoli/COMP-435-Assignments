from scapy.all import *

A = "192.0.2.0" # spoofed source IP address
B = "127.0.0.1" # destination IP address
C = 1000 # source port
D = 23 # destination port
payload = "hello mah dewd" # packet payload

spoofed_packet = IP(src=A, dst=B) / TCP(sport=C, dport=D) / payload
send(spoofed_packet) # sends the custom packet to scapy
