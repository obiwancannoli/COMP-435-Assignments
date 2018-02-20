from scapy.all import *

A = "1:02:03:04:05:06" # spoofed source MAC address

spoofed_packet = Ether(src=A)
send(spoofed_packet) # sends the spoofed packet through Scapy
