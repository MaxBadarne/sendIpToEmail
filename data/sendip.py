import requests
import datetime
import os
# get all the adresses and whatever is needed
now = datetime.datetime.now()
x = requests.get('http://ip.42.pl/raw').text
y = requests.get('http://jsonip.com').text
# Log Writer
def writelogf(x,y):
	logf = open("data/logs/log.txt" , "a")
	bigStringToWrite = str("Time and date: "+ str(now)+ "\n" + "Public IPv4 Adress : " + x + "\n" + "Public IPv6 Adress is :"+ y + "\n \n \n")
	logf.write(bigStringToWrite)
	logf.close()
# Create a temporarly file that will be later sent
def writesendf(x,y):
	sendf = open("data/temp.txt" ,"w")
	bigStringToWrite = str('"""' +"\n" +"Time and date: " +str(now) + "\n" +"Public IPv4 Adress : " +x +"\n" +"Public IPv6 Adress is :" +y +"\n" +'"""')
	sendf.write(bigStringToWrite)
	sendf.close()
# this function is only used when the Display is on
def printinfo(x,y):
	print("printing to file following information", "\nCurrent date and time: ",str(now), "\npublic  IPv4 adress : " ,x , "\npublic IPv6 Adress is : ", y )

def do():
	writesendf(x,y)
	writelogf(x,y)
	printinfo(x,y)
def do_no_terminal():
	writelogf(x,y)
	writesendf(x,y)