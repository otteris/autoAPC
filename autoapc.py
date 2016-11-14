#Modules

import os, sys, time;

#Variables

space = " "

print("DISCLAIMER: The creator of this tool, is not responsible for anything YOU do with this!")
for i in range(3):
	print(" ")

#Put the network interface into monitor mode

print("Enter your network interface:  ")
print("(If you dont know it, read the TUTORIAL.txt file)")
print("If already on monitor mode dont enter anything")
netif = input("Network interface: ")
print("Going into monitor mode....   ")
time.sleep(2)

#Kill processes that interfere with monitor mode 

os.system("airmon-ng check kill")
os.system ("airmon-ng start {}".format(netif))
os.system("airmon-ng")

#Assign new network interface that's in monitor mode

print("Type your new network interface. (Should look like ")
print(" wlan0mon, mon0, eth0mon, ")

#Set options to the fake access point

newnetif = input("NEW network interface:  ")
name = input("The essid/name for the fake wifi: ")

#Fake wifi is created

print("DO NOT EXIT THE SCRIPT OR THE WIFI WILL NOT BE CREATED")
time.sleep(1)
os.system("airbase-ng -c 1 -e {}".format(name)+(space)+(newnetif))



