#! /usr/bin/env python
import sys, os
from scapy.all import *
#txt file with a list
#remove \n
#get name of image to create
name_img = raw_input('enter in name for image: ')
askfile = raw_input('use file for server list? yes/no: ')
if askfile == "yes":
	serverfile = open("/root/python/scapy/fromfile/servers", "r")
	servers = [line[:-1] for line in serverfile]
elif askfile == "no":
	servers = []
	userin = raw_input("enter in domain/ip: ")
#	servers.append(userin)
	servers = userin.split()

#portsin = raw_input('ports= ')
#portsin = portsin.split()


print servers
#print portsin



#wiere you want svg and pngs to poop out
path="/home/pronto/images/scapy/"
#scapy stuff off for testing
res,unans=traceroute(servers[0:],dport=[80,443],maxttl=20,retry=-2)
res.graph(target="> %s%s.svg" % (path,name_img))
print "made"
os.system("chown pronto:users %s*" % path)
print "chowned"
os.system("rsvg %s%s.svg %s%s.png" % (path, name_img, path, name_img))
print "convreted"
#os.system("scp %s%s.png prontoco@pronto185.com:/home/prontoco/public_html/linux/scapy/" % (path,name_img))
print "http://pronto185.com/linux/scapy/" + name_img + ".png\n"
