#!/usr/bin/env python2.7
import os, sys, pexpect, urllib2

#needs a file called dirs.t  that lists one folder per new line
if os.path.isfile("./dirs.t") == False:
	quit("no dirs file")
file_dir = open('./dirs.t','r')
#url = "http://192.168.2.179/"
url = "http://pronto185.com/"
def GetHttpCode(url,folder):
	try:
		content = urllib2.urlopen(url+folder)
		return content.getcode(), content.read(60)
	except urllib2.HTTPError, e:
		code = e.getcode()
		return code, "null"

for line in file_dir.readlines():
	code = GetHttpCode(url,line)
	
	if code[0] != 404:
		print '%s	%s%s' % (str(code[0]),str(url),str(line.replace('\n','')))
		if code[0] == 200:
			print "\t\tFirst 60 char:\t" + code[1].replace("\n","")

