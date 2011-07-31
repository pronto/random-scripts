#!/usr/bin/env python2.7
#this does not work yet
import scapy

import random
source_port = random.randrange(60000,65000)
syn = IP(dst='pronto185.com')/TCP(dport=80, flags='S',sport=source_port)
syn_ack = sr1(syn)
#getStr = 'GET /ohhi HTTP/1.1\r\nHost: pronto185.com\r\n'
getStr = 'GET /ohhi HTTP/1.1\r\nHost: pronto185.com\r\nUser-Agent: Mozilla/5.0 (X11; bagels\r\n'
request = IP(dst='pronto185.com') / TCP(dport=80, sport=syn_ack[TCP].dport, seq=syn_ack[TCP].ack, ack=syn_ack[TCP].seq + 1, flags='A') / getStr
reply = sr1(request)

#<Ie  version=4L ihl=5L tos=0x0 len=44 id=424 flags= frag=0L ttl=55 proto=tcp chksum=0x2caa src=74.125.226.148 dst=10.20.30.40 options=[] |<TCP  sport=dport=ftp_data seq=3833491143 ack=1 dataofs=6L reserved=0L flags=SA window=5720 chksum=0xd8b6 urgptr=0 options=[('MSS', 1430)] |<Padding  load='\x00\x00' |>>>


