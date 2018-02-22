#!/usr/bin/env python

import socket, subprocess,sys
import os 
from netaddr import *
import paramiko,time, threading



subprocess.call('clear',shell=True)

def print_menu():
	print 30 * "-", "MENU", 30 * "-"
	print "1. Scan IP Address Ports"
	print "2. Brute Force SSH"
	print "3. Show Brute Force SSH file.log"
	print "4. List dict.txt"
	print "5. clear the screen"
	print "6. Exit"
	print 67 * "-"

loop=True
while loop:
	print_menu()
	try:
		choice =input("Enter your choice [1-6]:")
	
		if choice==1:
			rmip = raw_input("\t enter your ip address: ")
			r1 = int(raw_input("\t enter start port :\t"))
			r2 = int(raw_input("\t enter end port :\t"))

			try:
				for port in range(r1,r2):      	
            				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            				socket.setdefaulttimeout(1)
            				result = sock.connect_ex((rmip, port))
            				if result == 0:
                				print "  [-] Port Open: --->\t", port
            				sock.close()
			except KeyboardInterrupt:
       				print "You stop this "
        			sys.exit()
			except socket.gaierror:
        			print "Hostname could not be resolved"
       				sys.exit()
			except socket.error:
        			print "could not connect to server"
        			sys.exit()

		elif choice==2:
			ssh_brute = raw_input("eg. python ssh_try.py ip_address  dict.txt :")
			os.system(ssh_brute)


		elif choice==3:
                        print 30 * "+", "file.log", 30 * "+"
			os.system('cat file.log')
			print 67 * "+"

		elif choice==4:
                        print 30 * "*", "dict.txt", 30 * "*"
                        os.system('cat dict.txt')
                        print 67 * "*"

		elif choice==5:
			os.system('clear')

		elif choice==6:
			print "You decided to Exit .."
			loop=False


		else:
			raw_input("wrong option...")

	except KeyboardInterrupt:
		print "You exit .."
		sys.exit()

	except :
		print "try again"
