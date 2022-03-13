import requests
import datetime
import os
now = datetime.datetime.now()
x = requests.get('http://ip.42.pl/raw').text
y = requests.get('http://jsonip.com').text

sendf = open("temp.txt" ,"w")
def writelogf(x,y):
	logf = open("data/logs/log.txt" , "a")
	logf.write("Time and date: ")
	logf.write(str(now))
	logf.write("\n")
	logf.write("Public IPv4 Adress : ")
	logf.write(x)
	logf.write("\n")
	logf.write("Public IPv6 Adress is :")
	logf.write(y)
	logf.write("\n \n \n")
	logf.close()
	
def writesendf(x,y):
	sendf = open("temp.txt" ,"w")
	sendf.write('"""')
	sendf.write("\n")
	sendf.write("Time and date: ")
	sendf.write(str(now))
	sendf.write("\n")
	sendf.write("Public IPv4 Adress : ")
	sendf.write(x)
	sendf.write("\n")
	sendf.write("Public IPv6 Adress is :")
	sendf.write(y)
	sendf.write("\n")
	sendf.write('"""')
	sendf.close()
	
def printinfo(x,y):
	print("printing to file following information")
	print("Current date and time: ")
	print("public  IPv4 adress : " ,x)
	print("public IPv6 Adress is : ", y)

def do():
	writelogf(x,y)
	writesendf(x,y)
	printinfo(x,y)
def donp():
	writelogf(x,y)
	writesendf(x,y)


	
	


