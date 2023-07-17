import time
from data import getip
from data import sendemail
from data import private 
import os
import traceback
import logging

def run():
	if(private.TerminalActivated):
		getip.do()
		print(sendemail.sendip())
	else:
		getip.do_no_terminal()
		sendemail.sendip()
	time.sleep(1)      
	time.sleep(private.timetowait)

# in case of no connection, The script will keep trying to connect every second and then send the address
while(True): 
	try:
		time.sleep(1)
		run()
	except Exception as e:
    		logging.error(traceback.format_exc())