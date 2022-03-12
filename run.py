import time
from data import sendip
from data import sendemail
from data import private 
import os
while(True):
	sendip.do()
	sendemail.sendip()
	os.remove("temp.txt")                        
	time.sleep(86400)
	
        
