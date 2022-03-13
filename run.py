import time
from data import sendip
from data import sendemail
from data import private 
import os
import traceback
import logging
def run():
	sendip.do()
	sendemail.sendip()
	os.remove("temp.txt")                        
	time.sleep(private.timetowait)
	
        
while(True):
	try:
		time.sleep(1)
		run()
	except Exception as e:
    		logging.error(traceback.format_exc())
    # Logs the error appropriately. 
	
