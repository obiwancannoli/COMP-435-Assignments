from scapy.all import *

A = "192.0.2.0" # source address
B = "192.0.2.24" # destination address
payload = "Potatos have tons of carbs" # payload content



spoofed_packet = IP(src=A, dst=B) / ICMP() / payload
send(spoofed_packet) # sends the custom packet through scapy
