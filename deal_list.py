#!/usr/bin/python


ip_addr =[
'192.168.1.1',
'192.168.1.2',
'192.168.1.3',
'192.168.1.4']
user = [
'admin',
'admin',
'admin',
'admin']
password = [
'password1',
'password2',
'password3',
'password4']
customer = [
'AVIVA',
'Panasonic',
'DWP',
'Thomas Cook']



for x, y, z, n in map(None,ip_addr,user, password, customer):
	print "Ip-ul %s cu userul %s , parola %s si customerul %s " % (x, y, z, n)
        print "this is a test %s %s %s %s " % (x, y, z, n)
 
