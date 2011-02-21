#! /usr/bin/env python
# arping2tex : arpings a network and outputs a LaTeX table as a result

import sys, re, subprocess
#if len(sys.argv) != 2:
#    print "Usage: arping2tex <net>\n  eg: arping2tex 192.168.1.0/24"
#    sys.exit(1)
p = subprocess.Popen(["route"], stdout=subprocess.PIPE)
output1 = p.stdout.read().split('\n')
output2 = output1[2].split(' ')
netinfo = filter(None, output2)
#print netinfo 
#['192.168.2.0', '*', '255.255.255.0', 'U', '0', '0', '0', 'eth0']

if netinfo[2] == "255.255.255.0":
    cidr = "24"
elif netinfo[2] == "255.255.255.128":
    cidr = "25"
elif netinfo[2] == "255.255.255.192":
    cidr = "26"
elif netinfo[2] == "255.255.255.224":
    cidr = "27"
elif netinfo[2] == "255.255.255.240":
    cidr = "28"
elif netinfo[2] == "255.255.255.248":
    cidr = "29"
elif netinfo[2] == "255.255.255.32":
    cidr = "30"
network = netinfo[0]+"/"+cidr
print network
from scapy.all import srp,Ether,ARP,conf
conf.verb=0
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network),
              timeout=2)

for snd,rcv in ans:
	#print "test:" + Ether.src + "\n"
	mac = rcv.sprintf(r"%Ether.src%")
	ip = rcv.sprintf(r"%ARP.psrc%")
	for line in open("/root/python/mdb"):
		if mac[:8].upper() in line:
			info1 = re.sub("\n", "", line)
			info = re.sub(mac[:8].upper(), "" ,info1)
	#		print mac + " | " +  " | " + info + " | "
	#	else:
	#		info = "NOT FOUND IN DATABSE"

	print ip + " \t " + mac + " \t " + info  
	#print mac[:8]  #woo, THIS FUCKING WORKS , BITCH >:O
	#print rcv.sprintf(r"%Ether.src% & %ARP.psrc%\\")

