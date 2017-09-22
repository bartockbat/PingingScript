#!/usr/bin/python3

import sys, os, time 

from subprocess import call

x=1
while x <= 6: # performing the operation 6 times at 10 second intervals
	print("Pinging omniti.com\n")
	os.system("ping -c 2 omniti.com") #ping first server
	print("Pinging surge.omniti.com\n")
	os.system("ping -c 2 surge.omniti.com") #ping second server
	print("Pinging ansible-dk.org\n")
	os.system("ping -c 2 ansible-dk.org") #ping 3rd server
	x = x + 1
	print("waiting 10 seconds...") #wait 10 seconds
	time.sleep(10)
	os.system("clear")
	if x == 7:
	   print("We're done!") #Tell the audience you are done!
	   break
	else:
           continue
