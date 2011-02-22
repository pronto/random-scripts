#!/usr/bin/env python
import argparse, sys, re, subprocess, gzip

#change this to whre you have your file, i'll look into making this be auto later
path_to_mdb = "/home/pronto/git/random-scripts/arp/"

parser = argparse.ArgumentParser()
parser.add_argument('-i', action='store', dest='iface', default='AUTO', help='force the interface')
parser.add_argument('-n', action='store', dest='network', default='AUTO', help='force the network ex: 192.168.2.0/24')
results = parser.parse_args()
print results.iface
print results.network

num_box = 0
p = subprocess.Popen(["route"], stdout=subprocess.PIPE)
output1 = p.stdout.read().split('\n')
output2 = output1[2].split(' ')
netinfo = filter(None, output2)
#print netinfo 
#       0         1         2           3    4    5    6      7
#['192.168.2.0', '*', '255.255.255.0', 'U', '0', '0', '0', 'eth0']
# thanks to TorrentialStorm  we no longer have a massive elif table :D   *high five*
def calcCIDR(mask):
    mask = mask.split('.')
    bits = []
    for c in mask:
       bits.append(bin(int(c)))
    bits = ''.join(bits)
    cidr = 0
    for c in bits:
        if c == '1': cidr += 1
    return str(cidr)
if results.network == 'AUTO':
	cidr = calcCIDR(netinfo[2])
	network = netinfo[0]+"/"+cidr
else:
	network = results.network

print 'network/cidr: ' + network
conf.verb=0
if results.iface == 'AUTO':
	intface = netinfo[7]
else:
	intface = results.iface

print 'intface: ' + intface

from scapy.all import srp,Ether,ARP,conf
ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network), timeout=2, iface=intface)

for snd,rcv in ans:
    #print "test:" + Ether.src + "\n"
	mac = rcv.sprintf(r"%Ether.src%")
	ip = rcv.sprintf(r"%ARP.psrc%")
	for line in open(path_to_mdb+"mdb"):
	#   using the gzip makes it SLOW AS BALLS, but also makes mdb file from 1008k to 292k... tempting, but omg slow 
	#    for line in gzip.open(path_to_mdb+"mdb2.gz"):
		if mac[:8].upper() in line:
			info1 = re.sub("\n", "", line)
			info = re.sub(mac[:8].upper(), "" ,info1)
    #       print mac + " | " +  " | " + info + " | "
    #   else:
    #       info = "NOT FOUND IN DATABSE"
	num_box += 1
	print ip + " \t " + mac + " \t " + info.split(" ")[0]
    #print mac[:8]  #woo, THIS FUCKING WORKS , BITCH >:O
    #print rcv.sprintf(r"%Ether.src% & %ARP.psrc%\\")
print "total boxes: " + str(num_box)



