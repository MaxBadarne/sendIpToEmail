import time
from data import sendip
from data import sendemail
from data import private 
import os
import traceback
import logging

def run():
	if(private.TerminalActivated):
		sendip.do()
	else:
		sendip.do_no_terminal()
	sendemail.sendip()
	os.remove("temp.txt")                        
	time.sleep(private.timetowait)

# in case of no connection, The script will keep trying to connect every second and then send the address
while(True): 
	try:
		time.sleep(1)
		run()
	except Exception as e:
    		logging.error(traceback.format_exc())