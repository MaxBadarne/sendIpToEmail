import requests
import datetime
import os
# get all the adresses and whatever is needed
now = datetime.datetime.now()
Ipv4Adress = requests.get('http://ip.42.pl/raw').text
Ipv6Adress = requests.get('http://jsonip.com').text
# Log Writer
def writelogf(Ipv4Adress,Ipv6Adress):
	logf = open("data/logs/log.txt" , "a")
	bigStringToWrite = str("Time and date: "+ str(now)+ "\n" + "Public IPv4 Adress : " + Ipv4Adress + "\n" + "Public IPv6 Adress is :"+ Ipv6Adress + "\n \n \n")
	logf.write(bigStringToWrite)
	logf.close()
# Create a temporarly file that will be later sent
def writesendf(Ipv4Adress,Ipv6Adress):
	sendf = open("data/temp.txt" ,"w")
	bigStringToWrite = str('"""' +"\n" +"Time and date: " +str(now) + "\n" +"Public IPv4 Adress : " +Ipv4Adress +"\n" +"Public IPv6 Adress is :" +Ipv6Adress +"\n" +'"""')
	sendf.write(bigStringToWrite)
	sendf.close()
# this function is only used when the Display is on
def printinfo(Ipv4Adress,Ipv6Adress):
	print("printing to file following information", "\nCurrent date and time: ",str(now), "\npublic  IPv4 adress : " ,Ipv4Adress , "\npublic IPv6 Adress is : ", Ipv6Adress )

def do():
	writesendf(Ipv4Adress,Ipv6Adress)
	writelogf(Ipv4Adress,Ipv6Adress)
	printinfo(Ipv4Adress,Ipv6Adress)
def do_no_terminal():
	writelogf(Ipv4Adress,Ipv6Adress)
	writesendf(Ipv4Adress,Ipv6Adress)