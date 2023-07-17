def clearlog():
    logf = open("data/logs/log.txt" , "w")
    logf.write("")
    logf.close()
def clearTemp():
    sendf = open("data/temp.txt" ,"w")
    sendf.write("")
    sendf.close()
def resetSettings():
    x = open("data/private.py", "w")
    x.write('timetowait = 86400 \n')
    x.write('apikey = "" \n')
    x.write('signupemail = ""\n')
    x.write('recieveradress = ""\n')
    x.write('TerminalActivated = True\n')
clearlog()
clearTemp()
resetSettings()