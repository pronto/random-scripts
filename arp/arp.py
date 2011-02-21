#! /usr/bin/env python
# arping2tex : arpings a network and outputs a LaTeX table as a result

import sys, re, subprocess
if len(sys.argv) != 2:
    print "Usage: arping2tex <net>\n  eg: arping2tex 192.168.1.0/24"
    sys.exit(1)

from scapy.all import srp,Ether,ARP,conf
conf.verb=0
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]),
              timeout=2)

for snd,rcv in ans:
	#print "test:" + Ether.src + "\n"
	mac = rcv.sprintf(r"%Ether.src%")
	ip = rcv.sprintf(r"%ARP.psrc%")
	for line in open("/home/pronto/git/random-scripts/arp/mdb"):
		if mac[:8].upper() in line:
			info1 = re.sub("\n", "", line)
			info = re.sub(mac[:8].upper(), "" ,info1)
	#		print mac + " | " +  " | " + info + " | "
	#	else:
	#		info = "NOT FOUND IN DATABSE"

	print ip + " \t " + mac + " \t " + info  
	#print mac[:8]  #woo, THIS FUCKING WORKS , BITCH >:O
	#print rcv.sprintf(r"%Ether.src% & %ARP.psrc%\\")

