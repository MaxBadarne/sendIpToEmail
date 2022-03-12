import smtplib, ssl
from data import private 

def sendip():
	sendf = open("temp.txt" ,"r")
	ip = sendf.read()
	port = 465  # For SSL
	smtp_server = "smtp.gmail.com"
	sender_email = private.senderadress
	receiver_email = private.recieveradress
	password = private.password
	message = ip 
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	    server.login(sender_email, password)
	    server.sendmail(sender_email, receiver_email, message)

